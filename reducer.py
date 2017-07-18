#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import boto3
import sys

AWS_ACCESS_KEY_ID = "AKIAIQWIVEDREFE6BURA"
AWS_SECRET_ACCESS_KEY = "t9bq0jkefSMt7Oa0uRJzEHEjvPtz7zyZ3QtD0zMS"
bucket = "common-crawl-extracted-urls"
filename = "sample1.txt"


def read_mapper_output(filename, separator='\t'):
    for line in filename:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    urls = []
    for current_url, group in groupby(data, itemgetter(0)):
        try:
            urls.append(current_url + "\n")
        except ValueError:
            pass
    # write list to file on s3
    s3 = boto3.resource("s3")
    s3.Bucket(bucket).put_object(Key=filename, Body="".join(urls))


if __name__ == "__main__":
    main()
