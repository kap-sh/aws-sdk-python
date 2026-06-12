"""Generated from Smithy shape ``com.amazonaws.glue#OverwriteChildResourcePermissionsWithDefaultEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

OverwriteChildResourcePermissionsWithDefaultEnum: TypeAlias = Literal[
    "Accept",
    "Deny",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Accept",
        "Deny",
    )
)


def serialize_aws_json_1_1(
    value: OverwriteChildResourcePermissionsWithDefaultEnum,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> OverwriteChildResourcePermissionsWithDefaultEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OverwriteChildResourcePermissionsWithDefaultEnum value: {data!r}"
        )
    return cast(OverwriteChildResourcePermissionsWithDefaultEnum, data)
