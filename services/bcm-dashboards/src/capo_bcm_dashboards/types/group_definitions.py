"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GroupDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.group_definition

GroupDefinitions: TypeAlias = list[
    "capo_bcm_dashboards.types.group_definition.GroupDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GroupDefinitions) -> list:
    import capo_bcm_dashboards.types.group_definition

    out: list = []
    for item in value:
        out.append(
            capo_bcm_dashboards.types.group_definition.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GroupDefinitions:
    import capo_bcm_dashboards.types.group_definition

    out: GroupDefinitions = []
    for item in data:
        out.append(
            capo_bcm_dashboards.types.group_definition.deserialize_aws_json_1_0(item)
        )
    return out
