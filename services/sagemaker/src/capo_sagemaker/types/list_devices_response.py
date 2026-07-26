"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_summaries
    import capo_sagemaker.types.next_token


class ListDevicesResponse(TypedDict, closed=True):
    device_summaries: NotRequired[
        "capo_sagemaker.types.device_summaries.DeviceSummaries"
    ]
    """<p>Summary of devices.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesResponse) -> dict:
    out: dict = {}
    if "device_summaries" in value:
        import capo_sagemaker.types.device_summaries

        out["DeviceSummaries"] = (
            capo_sagemaker.types.device_summaries.serialize_aws_json_1_1(
                value["device_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesResponse:
    out: ListDevicesResponse = {}  # type: ignore[typeddict-item]
    if "DeviceSummaries" in data:
        import capo_sagemaker.types.device_summaries

        out["device_summaries"] = (
            capo_sagemaker.types.device_summaries.deserialize_aws_json_1_1(
                data["DeviceSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
