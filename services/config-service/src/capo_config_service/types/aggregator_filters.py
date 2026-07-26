"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.aggregator_filter_resource_type
    import capo_config_service.types.aggregator_filter_service_principal


class AggregatorFilters(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_config_service.types.aggregator_filter_resource_type.AggregatorFilterResourceType"
    ]
    """<p>An object to filter the configuration recorders based on the resource types in scope for recording.</p>"""
    service_principal: NotRequired[
        "capo_config_service.types.aggregator_filter_service_principal.AggregatorFilterServicePrincipal"
    ]
    """<p>An object to filter service-linked configuration recorders in an aggregator based on the linked Amazon Web Services service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatorFilters) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_config_service.types.aggregator_filter_resource_type

        out["ResourceType"] = (
            capo_config_service.types.aggregator_filter_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "service_principal" in value:
        import capo_config_service.types.aggregator_filter_service_principal

        out["ServicePrincipal"] = (
            capo_config_service.types.aggregator_filter_service_principal.serialize_aws_json_1_1(
                value["service_principal"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatorFilters:
    out: AggregatorFilters = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_config_service.types.aggregator_filter_resource_type

        out["resource_type"] = (
            capo_config_service.types.aggregator_filter_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "ServicePrincipal" in data:
        import capo_config_service.types.aggregator_filter_service_principal

        out["service_principal"] = (
            capo_config_service.types.aggregator_filter_service_principal.deserialize_aws_json_1_1(
                data["ServicePrincipal"]
            )
        )
    return out
