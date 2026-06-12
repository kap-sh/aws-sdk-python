"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFormationStackOutputsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details

AwsCloudFormationStackOutputsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details.AwsCloudFormationStackOutputsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFormationStackOutputsList) -> list:
    import aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCloudFormationStackOutputsList:
    import aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details

    out: AwsCloudFormationStackOutputsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_cloud_formation_stack_outputs_details.deserialize_json(
                item
            )
        )
    return out
