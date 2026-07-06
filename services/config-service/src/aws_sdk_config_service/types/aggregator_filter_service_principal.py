"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorFilterServicePrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregator_filter_type
    import aws_sdk_config_service.types.service_principal_value_list


class AggregatorFilterServicePrincipal(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_config_service.types.aggregator_filter_type.AggregatorFilterType"
    ]
    """<p>The type of service principal filter to apply. <code>INCLUDE</code> specifies that the list of service principals in the <code>Value</code> field will be aggregated and no other service principals will be filtered.</p>"""
    value: NotRequired[
        "aws_sdk_config_service.types.service_principal_value_list.ServicePrincipalValueList"
    ]
    """<p>Comma-separated list of service principals for the linked Amazon Web Services services to filter your aggregated service-linked configuration recorders.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatorFilterServicePrincipal) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_config_service.types.aggregator_filter_type

        out["Type"] = (
            aws_sdk_config_service.types.aggregator_filter_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        import aws_sdk_config_service.types.service_principal_value_list

        out["Value"] = (
            aws_sdk_config_service.types.service_principal_value_list.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatorFilterServicePrincipal:
    out: AggregatorFilterServicePrincipal = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_config_service.types.aggregator_filter_type

        out["type"] = (
            aws_sdk_config_service.types.aggregator_filter_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        import aws_sdk_config_service.types.service_principal_value_list

        out["value"] = (
            aws_sdk_config_service.types.service_principal_value_list.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    return out
