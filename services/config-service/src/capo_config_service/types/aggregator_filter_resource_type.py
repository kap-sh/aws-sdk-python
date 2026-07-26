"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorFilterResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.aggregator_filter_type
    import capo_config_service.types.resource_type_value_list


class AggregatorFilterResourceType(TypedDict, closed=True):
    type: NotRequired[
        "capo_config_service.types.aggregator_filter_type.AggregatorFilterType"
    ]
    """<p>The type of resource type filter to apply. <code>INCLUDE</code> specifies that the list of resource types in the <code>Value</code> field will be aggregated and no other resource types will be filtered.</p>"""
    value: NotRequired[
        "capo_config_service.types.resource_type_value_list.ResourceTypeValueList"
    ]
    """<p>Comma-separate list of resource types to filter your aggregated configuration recorders.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatorFilterResourceType) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_config_service.types.aggregator_filter_type

        out["Type"] = (
            capo_config_service.types.aggregator_filter_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        import capo_config_service.types.resource_type_value_list

        out["Value"] = (
            capo_config_service.types.resource_type_value_list.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatorFilterResourceType:
    out: AggregatorFilterResourceType = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_config_service.types.aggregator_filter_type

        out["type"] = (
            capo_config_service.types.aggregator_filter_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        import capo_config_service.types.resource_type_value_list

        out["value"] = (
            capo_config_service.types.resource_type_value_list.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    return out
