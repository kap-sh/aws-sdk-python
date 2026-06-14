"""Generated from Smithy shape ``com.amazonaws.workspaces#StreamingExperiencePreferredProtocolEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

StreamingExperiencePreferredProtocolEnum: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "UDP",
    )
)


def serialize_aws_json_1_1(value: StreamingExperiencePreferredProtocolEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamingExperiencePreferredProtocolEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StreamingExperiencePreferredProtocolEnum value: {data!r}"
        )
    return cast(StreamingExperiencePreferredProtocolEnum, data)
