"""Generated from Smithy shape ``com.amazonaws.sfn#StateMachineVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.state_machine_version_list_item

StateMachineVersionList: TypeAlias = list[
    "aws_sdk_sfn.types.state_machine_version_list_item.StateMachineVersionListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateMachineVersionList) -> list:
    import aws_sdk_sfn.types.state_machine_version_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sfn.types.state_machine_version_list_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StateMachineVersionList:
    import aws_sdk_sfn.types.state_machine_version_list_item

    out: StateMachineVersionList = []
    for item in data:
        out.append(
            aws_sdk_sfn.types.state_machine_version_list_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
