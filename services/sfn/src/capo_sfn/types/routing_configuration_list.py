"""Generated from Smithy shape ``com.amazonaws.sfn#RoutingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.routing_configuration_list_item

RoutingConfigurationList: TypeAlias = list[
    "capo_sfn.types.routing_configuration_list_item.RoutingConfigurationListItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingConfigurationList) -> list:
    import capo_sfn.types.routing_configuration_list_item

    out: list = []
    for item in value:
        out.append(
            capo_sfn.types.routing_configuration_list_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RoutingConfigurationList:
    import capo_sfn.types.routing_configuration_list_item

    out: RoutingConfigurationList = []
    for item in data:
        out.append(
            capo_sfn.types.routing_configuration_list_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
