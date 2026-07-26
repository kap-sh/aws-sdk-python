"""Generated from Smithy shape ``com.amazonaws.glue#OverwriteChildResourcePermissionsWithDefaultEnum``."""

from typing import Literal, TypeAlias, cast

OverwriteChildResourcePermissionsWithDefaultEnum: TypeAlias = Literal[
    "Accept",
    "Deny",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: OverwriteChildResourcePermissionsWithDefaultEnum,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> OverwriteChildResourcePermissionsWithDefaultEnum:
    return cast(OverwriteChildResourcePermissionsWithDefaultEnum, data)
