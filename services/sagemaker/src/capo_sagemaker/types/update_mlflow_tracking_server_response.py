"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMlflowTrackingServerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.tracking_server_arn


class UpdateMlflowTrackingServerResponse(TypedDict, closed=True):
    tracking_server_arn: NotRequired[
        "capo_sagemaker.types.tracking_server_arn.TrackingServerArn"
    ]
    """<p>The ARN of the updated MLflow Tracking Server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMlflowTrackingServerResponse) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["TrackingServerArn"] = value["tracking_server_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMlflowTrackingServerResponse:
    out: UpdateMlflowTrackingServerResponse = {}  # type: ignore[typeddict-item]
    if "TrackingServerArn" in data:
        out["tracking_server_arn"] = data["TrackingServerArn"]
    return out
