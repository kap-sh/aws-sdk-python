"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_arn
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.string1024


class CreateDomainResponse(TypedDict):
    domain_arn: NotRequired["aws_sdk_sagemaker.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the created domain.</p>"""
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the created domain.</p>"""
    url: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The URL to the created domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDomainResponse) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDomainResponse:
    out: CreateDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "Url" in data:
        out["url"] = data["Url"]
    return out
