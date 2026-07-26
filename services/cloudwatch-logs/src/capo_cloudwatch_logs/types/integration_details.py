"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.open_search_integration_details


class _IntegrationDetails_openSearchIntegrationDetails(TypedDict, closed=True):
    openSearchIntegrationDetails: "capo_cloudwatch_logs.types.open_search_integration_details.OpenSearchIntegrationDetails"


IntegrationDetails: TypeAlias = _IntegrationDetails_openSearchIntegrationDetails


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationDetails) -> dict:
    if "openSearchIntegrationDetails" in value:
        import capo_cloudwatch_logs.types.open_search_integration_details

        return {
            "openSearchIntegrationDetails": capo_cloudwatch_logs.types.open_search_integration_details.serialize_aws_json_1_1(
                value["openSearchIntegrationDetails"]
            )
        }
    else:
        raise SerializationError("IntegrationDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> IntegrationDetails:
    if "openSearchIntegrationDetails" in data:
        import capo_cloudwatch_logs.types.open_search_integration_details

        return {
            "openSearchIntegrationDetails": capo_cloudwatch_logs.types.open_search_integration_details.deserialize_aws_json_1_1(
                data["openSearchIntegrationDetails"]
            )
        }
    else:
        raise DeserializationError("IntegrationDetails: no recognized variant key")
