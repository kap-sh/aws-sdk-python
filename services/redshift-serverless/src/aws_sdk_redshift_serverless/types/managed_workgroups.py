"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ManagedWorkgroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.managed_workgroup_list_item

ManagedWorkgroups: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.managed_workgroup_list_item.ManagedWorkgroupListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedWorkgroups) -> list:
    import aws_sdk_redshift_serverless.types.managed_workgroup_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.managed_workgroup_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedWorkgroups:
    import aws_sdk_redshift_serverless.types.managed_workgroup_list_item

    out: ManagedWorkgroups = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.managed_workgroup_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
