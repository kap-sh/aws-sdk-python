"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedMlflowAppUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.mlflow_app_url


class CreatePresignedMlflowAppUrlResponse(TypedDict, closed=True):
    authorized_url: NotRequired["capo_sagemaker.types.mlflow_app_url.MlflowAppUrl"]
    """<p>A presigned URL with an authorization token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedMlflowAppUrlResponse) -> dict:
    out: dict = {}
    if "authorized_url" in value:
        out["AuthorizedUrl"] = value["authorized_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedMlflowAppUrlResponse:
    out: CreatePresignedMlflowAppUrlResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrl" in data:
        out["authorized_url"] = data["AuthorizedUrl"]
    return out
