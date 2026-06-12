"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.operating_system_name

OperatingSystemNameList: TypeAlias = list[
    "aws_sdk_workspaces.types.operating_system_name.OperatingSystemName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemNameList) -> list:
    import aws_sdk_workspaces.types.operating_system_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.operating_system_name.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperatingSystemNameList:
    import aws_sdk_workspaces.types.operating_system_name

    out: OperatingSystemNameList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.operating_system_name.deserialize_aws_json_1_1(
                item
            )
        )
    return out
