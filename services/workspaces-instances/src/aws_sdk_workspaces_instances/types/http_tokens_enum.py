"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HttpTokensEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

HttpTokensEnum: TypeAlias = Literal[
    "optional",
    "required",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "optional",
        "required",
    )
)


def serialize_aws_json_1_0(value: HttpTokensEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HttpTokensEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpTokensEnum value: {data!r}")
    return cast(HttpTokensEnum, data)
