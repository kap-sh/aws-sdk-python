"""Generated from Smithy shape ``com.amazonaws.s3#StreamingBlob``."""

from typing import TypeAlias

from aws_sdk_s3._iter import AnyIterator

StreamingBlob: TypeAlias = AnyIterator[bytes] | bytes
