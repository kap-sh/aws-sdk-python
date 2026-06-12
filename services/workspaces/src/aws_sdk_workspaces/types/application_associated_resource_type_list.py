"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationAssociatedResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_associated_resource_type

ApplicationAssociatedResourceTypeList: TypeAlias = list[
    "aws_sdk_workspaces.types.application_associated_resource_type.ApplicationAssociatedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssociatedResourceTypeList) -> list:
    import aws_sdk_workspaces.types.application_associated_resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.application_associated_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationAssociatedResourceTypeList:
    import aws_sdk_workspaces.types.application_associated_resource_type

    out: ApplicationAssociatedResourceTypeList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.application_associated_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
