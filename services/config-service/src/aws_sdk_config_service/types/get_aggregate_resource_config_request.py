"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_resource_identifier
    import aws_sdk_config_service.types.configuration_aggregator_name


class GetAggregateResourceConfigRequest(TypedDict):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    resource_identifier: "aws_sdk_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier"
    """<p>An object that identifies aggregate resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    import aws_sdk_config_service.types.aggregate_resource_identifier

    out["ResourceIdentifier"] = (
        aws_sdk_config_service.types.aggregate_resource_identifier.serialize_aws_json_1_1(
            value["resource_identifier"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAggregateResourceConfigRequest:
    out: GetAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "GetAggregateResourceConfigRequest.configuration_aggregator_name required"
        )
    if "ResourceIdentifier" in data:
        import aws_sdk_config_service.types.aggregate_resource_identifier

        out["resource_identifier"] = (
            aws_sdk_config_service.types.aggregate_resource_identifier.deserialize_aws_json_1_1(
                data["ResourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetAggregateResourceConfigRequest.resource_identifier required"
        )
    return out
