"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ActionOwner: TypeAlias = Literal[
    "AWS",
    "ThirdParty",
    "Custom",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "ThirdParty",
        "Custom",
    )
)


def serialize_aws_json_1_1(value: ActionOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionOwner value: {data!r}")
    return cast(ActionOwner, data)
