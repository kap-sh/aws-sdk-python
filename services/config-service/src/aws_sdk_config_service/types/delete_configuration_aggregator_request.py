"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteConfigurationAggregatorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_aggregator_name


class DeleteConfigurationAggregatorRequest(TypedDict):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConfigurationAggregatorRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConfigurationAggregatorRequest:
    out: DeleteConfigurationAggregatorRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "DeleteConfigurationAggregatorRequest.configuration_aggregator_name required"
        )
    return out
