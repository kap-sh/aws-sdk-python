"""Generated from Smithy shape ``com.amazonaws.configservice#BatchGetAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_aggregator_name
    import aws_sdk_config_service.types.resource_identifiers_list


class BatchGetAggregateResourceConfigRequest(TypedDict):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    resource_identifiers: (
        "aws_sdk_config_service.types.resource_identifiers_list.ResourceIdentifiersList"
    )
    """<p>A list of aggregate ResourceIdentifiers objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    import aws_sdk_config_service.types.resource_identifiers_list

    out["ResourceIdentifiers"] = (
        aws_sdk_config_service.types.resource_identifiers_list.serialize_aws_json_1_1(
            value["resource_identifiers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetAggregateResourceConfigRequest:
    out: BatchGetAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "BatchGetAggregateResourceConfigRequest.configuration_aggregator_name required"
        )
    if "ResourceIdentifiers" in data:
        import aws_sdk_config_service.types.resource_identifiers_list

        out["resource_identifiers"] = (
            aws_sdk_config_service.types.resource_identifiers_list.deserialize_aws_json_1_1(
                data["ResourceIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAggregateResourceConfigRequest.resource_identifiers required"
        )
    return out
