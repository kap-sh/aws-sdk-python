"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopMlflowTrackingServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.tracking_server_name


class StopMlflowTrackingServerRequest(TypedDict, closed=True):
    tracking_server_name: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the tracking server to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMlflowTrackingServerRequest) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMlflowTrackingServerRequest:
    out: StopMlflowTrackingServerRequest = {}  # type: ignore[typeddict-item]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    return out
