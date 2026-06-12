"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

MaintenanceWindowResourceType: TypeAlias = Literal[
    "INSTANCE",
    "RESOURCE_GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE",
        "RESOURCE_GROUP",
    )
)


def serialize_aws_json_1_1(value: MaintenanceWindowResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MaintenanceWindowResourceType value: {data!r}"
        )
    return cast(MaintenanceWindowResourceType, data)
