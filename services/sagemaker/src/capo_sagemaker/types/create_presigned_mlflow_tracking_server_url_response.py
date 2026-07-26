"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedMlflowTrackingServerUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.tracking_server_url


class CreatePresignedMlflowTrackingServerUrlResponse(TypedDict, closed=True):
    authorized_url: NotRequired[
        "capo_sagemaker.types.tracking_server_url.TrackingServerUrl"
    ]
    """<p>A presigned URL with an authorization token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreatePresignedMlflowTrackingServerUrlResponse,
) -> dict:
    out: dict = {}
    if "authorized_url" in value:
        out["AuthorizedUrl"] = value["authorized_url"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreatePresignedMlflowTrackingServerUrlResponse:
    out: CreatePresignedMlflowTrackingServerUrlResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrl" in data:
        out["authorized_url"] = data["AuthorizedUrl"]
    return out
