"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#ResponseStream``."""

from typing import TypeAlias

from aws_sdk_sagemakerjobruntime._iter import AnyIterator

"""Streaming response body composed of successive payload chunks."""
ResponseStream: TypeAlias = AnyIterator[bytes] | bytes
