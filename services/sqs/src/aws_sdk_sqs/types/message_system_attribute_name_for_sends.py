"""Generated from Smithy shape ``com.amazonaws.sqs#MessageSystemAttributeNameForSends``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sqs.errors import DeserializationError

MessageSystemAttributeNameForSends: TypeAlias = Literal["AWSTraceHeader",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWSTraceHeader",))


def serialize_aws_json_1_0(value: MessageSystemAttributeNameForSends) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MessageSystemAttributeNameForSends:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MessageSystemAttributeNameForSends value: {data!r}"
        )
    return cast(MessageSystemAttributeNameForSends, data)
