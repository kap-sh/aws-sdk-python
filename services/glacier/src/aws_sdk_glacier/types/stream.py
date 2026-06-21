"""Generated from Smithy shape ``com.amazonaws.glacier#Stream``."""

from typing import TypeAlias

from aws_sdk_glacier._iter import AnyIterator

Stream: TypeAlias = AnyIterator[bytes] | bytes
