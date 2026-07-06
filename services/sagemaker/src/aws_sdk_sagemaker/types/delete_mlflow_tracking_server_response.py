"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteMlflowTrackingServerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.tracking_server_arn


class DeleteMlflowTrackingServerResponse(TypedDict, closed=True):
    tracking_server_arn: NotRequired[
        "aws_sdk_sagemaker.types.tracking_server_arn.TrackingServerArn"
    ]
    """<p>A <code>TrackingServerArn</code> object, the ARN of the tracking server that is deleted if successfully found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMlflowTrackingServerResponse) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["TrackingServerArn"] = value["tracking_server_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMlflowTrackingServerResponse:
    out: DeleteMlflowTrackingServerResponse = {}  # type: ignore[typeddict-item]
    if "TrackingServerArn" in data:
        out["tracking_server_arn"] = data["TrackingServerArn"]
    return out
