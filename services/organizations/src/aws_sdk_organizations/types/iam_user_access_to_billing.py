"""Generated from Smithy shape ``com.amazonaws.organizations#IAMUserAccessToBilling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

IAMUserAccessToBilling: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: IAMUserAccessToBilling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IAMUserAccessToBilling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IAMUserAccessToBilling value: {data!r}")
    return cast(IAMUserAccessToBilling, data)
