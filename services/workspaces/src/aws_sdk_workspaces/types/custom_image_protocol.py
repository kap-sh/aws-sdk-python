"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomImageProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

CustomImageProtocol: TypeAlias = Literal[
    "PCOIP",
    "DCV",
    "BYOP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PCOIP",
        "DCV",
        "BYOP",
    )
)


def serialize_aws_json_1_1(value: CustomImageProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomImageProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomImageProtocol value: {data!r}")
    return cast(CustomImageProtocol, data)
