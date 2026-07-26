"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_arn


class UpdateDomainResponse(TypedDict, closed=True):
    domain_arn: NotRequired["capo_sagemaker.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainResponse) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDomainResponse:
    out: UpdateDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    return out
