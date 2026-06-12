"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet_config

InstanceFleetConfigList: TypeAlias = list[
    "aws_sdk_emr.types.instance_fleet_config.InstanceFleetConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetConfigList) -> list:
    import aws_sdk_emr.types.instance_fleet_config

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.instance_fleet_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceFleetConfigList:
    import aws_sdk_emr.types.instance_fleet_config

    out: InstanceFleetConfigList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.instance_fleet_config.deserialize_aws_json_1_1(item)
        )
    return out
