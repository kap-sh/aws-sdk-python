"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowIdentityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_identity

MaintenanceWindowIdentityList: TypeAlias = list[
    "aws_sdk_ssm.types.maintenance_window_identity.MaintenanceWindowIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowIdentityList) -> list:
    import aws_sdk_ssm.types.maintenance_window_identity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.maintenance_window_identity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowIdentityList:
    import aws_sdk_ssm.types.maintenance_window_identity

    out: MaintenanceWindowIdentityList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.maintenance_window_identity.deserialize_aws_json_1_1(item)
        )
    return out
