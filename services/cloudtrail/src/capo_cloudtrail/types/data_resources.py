"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DataResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.data_resource

DataResources: TypeAlias = list["capo_cloudtrail.types.data_resource.DataResource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataResources) -> list:
    import capo_cloudtrail.types.data_resource

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.data_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataResources:
    import capo_cloudtrail.types.data_resource

    out: DataResources = []
    for item in data:
        out.append(capo_cloudtrail.types.data_resource.deserialize_aws_json_1_1(item))
    return out
