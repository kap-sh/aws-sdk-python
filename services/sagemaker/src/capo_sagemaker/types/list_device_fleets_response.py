"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDeviceFleetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_fleet_summaries
    import capo_sagemaker.types.next_token


class ListDeviceFleetsResponse(TypedDict, closed=True):
    device_fleet_summaries: NotRequired[
        "capo_sagemaker.types.device_fleet_summaries.DeviceFleetSummaries"
    ]
    """<p>Summary of the device fleet.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeviceFleetsResponse) -> dict:
    out: dict = {}
    if "device_fleet_summaries" in value:
        import capo_sagemaker.types.device_fleet_summaries

        out["DeviceFleetSummaries"] = (
            capo_sagemaker.types.device_fleet_summaries.serialize_aws_json_1_1(
                value["device_fleet_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeviceFleetsResponse:
    out: ListDeviceFleetsResponse = {}  # type: ignore[typeddict-item]
    if "DeviceFleetSummaries" in data:
        import capo_sagemaker.types.device_fleet_summaries

        out["device_fleet_summaries"] = (
            capo_sagemaker.types.device_fleet_summaries.deserialize_aws_json_1_1(
                data["DeviceFleetSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
