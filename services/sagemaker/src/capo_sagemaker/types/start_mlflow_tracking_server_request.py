"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartMlflowTrackingServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.tracking_server_name


class StartMlflowTrackingServerRequest(TypedDict, closed=True):
    tracking_server_name: NotRequired[
        "capo_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the tracking server to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMlflowTrackingServerRequest) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMlflowTrackingServerRequest:
    out: StartMlflowTrackingServerRequest = {}  # type: ignore[typeddict-item]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    return out
