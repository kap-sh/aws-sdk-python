"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet

InstanceFleetList: TypeAlias = list["aws_sdk_emr.types.instance_fleet.InstanceFleet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetList) -> list:
    import aws_sdk_emr.types.instance_fleet

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.instance_fleet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceFleetList:
    import aws_sdk_emr.types.instance_fleet

    out: InstanceFleetList = []
    for item in data:
        out.append(aws_sdk_emr.types.instance_fleet.deserialize_aws_json_1_1(item))
    return out
