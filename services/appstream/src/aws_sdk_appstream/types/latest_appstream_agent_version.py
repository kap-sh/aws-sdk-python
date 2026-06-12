"""Generated from Smithy shape ``com.amazonaws.appstream#LatestAppstreamAgentVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

LatestAppstreamAgentVersion: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
    )
)


def serialize_aws_json_1_1(value: LatestAppstreamAgentVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LatestAppstreamAgentVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LatestAppstreamAgentVersion value: {data!r}"
        )
    return cast(LatestAppstreamAgentVersion, data)
