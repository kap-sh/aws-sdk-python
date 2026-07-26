"""Generated from Smithy shape ``com.amazonaws.emr#PlacementGroupConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.placement_group_config

PlacementGroupConfigList: TypeAlias = list[
    "capo_emr.types.placement_group_config.PlacementGroupConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementGroupConfigList) -> list:
    import capo_emr.types.placement_group_config

    out: list = []
    for item in value:
        out.append(capo_emr.types.placement_group_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlacementGroupConfigList:
    import capo_emr.types.placement_group_config

    out: PlacementGroupConfigList = []
    for item in data:
        out.append(capo_emr.types.placement_group_config.deserialize_aws_json_1_1(item))
    return out
