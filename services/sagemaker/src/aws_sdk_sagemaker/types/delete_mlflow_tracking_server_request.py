"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteMlflowTrackingServerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.tracking_server_name


class DeleteMlflowTrackingServerRequest(TypedDict):
    tracking_server_name: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>The name of the the tracking server to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMlflowTrackingServerRequest) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMlflowTrackingServerRequest:
    out: DeleteMlflowTrackingServerRequest = {}  # type: ignore[typeddict-item]
    if "TrackingServerName" in data:
        out["tracking_server_name"] = data["TrackingServerName"]
    return out
