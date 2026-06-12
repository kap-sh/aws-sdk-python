"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePresignedDomainUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.presigned_domain_url


class CreatePresignedDomainUrlResponse(TypedDict):
    authorized_url: NotRequired[
        "aws_sdk_sagemaker.types.presigned_domain_url.PresignedDomainUrl"
    ]
    """<p>The presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedDomainUrlResponse) -> dict:
    out: dict = {}
    if "authorized_url" in value:
        out["AuthorizedUrl"] = value["authorized_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedDomainUrlResponse:
    out: CreatePresignedDomainUrlResponse = {}  # type: ignore[typeddict-item]
    if "AuthorizedUrl" in data:
        out["authorized_url"] = data["AuthorizedUrl"]
    return out
