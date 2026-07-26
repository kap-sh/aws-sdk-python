"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowResourceType``."""

from typing import Literal, TypeAlias, cast

MaintenanceWindowResourceType: TypeAlias = Literal[
    "INSTANCE",
    "RESOURCE_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowResourceType:
    return cast(MaintenanceWindowResourceType, data)
