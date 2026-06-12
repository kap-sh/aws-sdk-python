"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePartnerAppPresignedUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string2048


class CreatePartnerAppPresignedUrlResponse(TypedDict):
    url: NotRequired["aws_sdk_sagemaker.types.string2048.String2048"]
    """<p>The presigned URL that you can use to access the SageMaker Partner AI App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartnerAppPresignedUrlResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartnerAppPresignedUrlResponse:
    out: CreatePartnerAppPresignedUrlResponse = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
