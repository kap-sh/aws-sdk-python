"""Generated from Smithy shape ``com.amazonaws.appstream#AgentSoftwareVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""The image type is the type of AppStream image resource."""
AgentSoftwareVersion: TypeAlias = Literal[
    "CURRENT_LATEST",
    "ALWAYS_LATEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT_LATEST",
        "ALWAYS_LATEST",
    )
)


def serialize_aws_json_1_1(value: AgentSoftwareVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentSoftwareVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentSoftwareVersion value: {data!r}")
    return cast(AgentSoftwareVersion, data)
