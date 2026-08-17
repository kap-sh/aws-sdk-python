"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.integration_status_message
    import capo_cloudwatch_logs.types.open_search_resource_status_type


class OpenSearchResourceStatus(TypedDict, closed=True):
    status: NotRequired[
        "capo_cloudwatch_logs.types.open_search_resource_status_type.OpenSearchResourceStatusType"
    ]
    """<p>The current status of this resource.</p>"""
    status_message: NotRequired[
        "capo_cloudwatch_logs.types.integration_status_message.IntegrationStatusMessage"
    ]
    """<p>A message with additional information about the status of this resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchResourceStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cloudwatch_logs.types.open_search_resource_status_type

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchResourceStatus:
    out: OpenSearchResourceStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.open_search_resource_status_type

        out["status"] = (
            capo_cloudwatch_logs.types.open_search_resource_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
