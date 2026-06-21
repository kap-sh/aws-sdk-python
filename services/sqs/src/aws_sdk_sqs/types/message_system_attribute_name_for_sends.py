"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeNameForSends``."""

from typing import Literal, TypeAlias, cast

MessageSystemAttributeNameForSends: TypeAlias = Literal["AWSTraceHeader",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageSystemAttributeNameForSends) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MessageSystemAttributeNameForSends:
    return cast(MessageSystemAttributeNameForSends, data)
