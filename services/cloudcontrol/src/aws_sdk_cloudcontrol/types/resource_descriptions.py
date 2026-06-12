"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.resource_description

ResourceDescriptions: TypeAlias = list[
    "aws_sdk_cloudcontrol.types.resource_description.ResourceDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDescriptions) -> list:
    import aws_sdk_cloudcontrol.types.resource_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudcontrol.types.resource_description.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceDescriptions:
    import aws_sdk_cloudcontrol.types.resource_description

    out: ResourceDescriptions = []
    for item in data:
        out.append(
            aws_sdk_cloudcontrol.types.resource_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
