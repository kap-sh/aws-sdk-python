"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigurationAggregatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator


class PutConfigurationAggregatorResponse(TypedDict, closed=True):
    configuration_aggregator: NotRequired[
        "capo_config_service.types.configuration_aggregator.ConfigurationAggregator"
    ]
    """<p>Returns a ConfigurationAggregator object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigurationAggregatorResponse) -> dict:
    out: dict = {}
    if "configuration_aggregator" in value:
        import capo_config_service.types.configuration_aggregator

        out["ConfigurationAggregator"] = (
            capo_config_service.types.configuration_aggregator.serialize_aws_json_1_1(
                value["configuration_aggregator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigurationAggregatorResponse:
    out: PutConfigurationAggregatorResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregator" in data:
        import capo_config_service.types.configuration_aggregator

        out["configuration_aggregator"] = (
            capo_config_service.types.configuration_aggregator.deserialize_aws_json_1_1(
                data["ConfigurationAggregator"]
            )
        )
    return out
