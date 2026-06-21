"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResponseStream``."""

from typing import TypeAlias

from aws_sdk_bedrock_agentcore._iter import AnyIterator

ResponseStream: TypeAlias = AnyIterator[bytes] | bytes
