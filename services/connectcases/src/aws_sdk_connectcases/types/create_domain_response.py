"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_arn
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.domain_status


class CreateDomainResponse(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    domain_arn: "aws_sdk_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) for the Cases domain.</p>"""
    domain_status: "aws_sdk_connectcases.types.domain_status.DomainStatus"
    """<p>The status of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainResponse) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["domainStatus"] = value["domain_status"]
    return out


def deserialize_json(data: dict) -> CreateDomainResponse:
    out: CreateDomainResponse = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateDomainResponse.domain_id required")
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError("CreateDomainResponse.domain_arn required")
    if "domainStatus" in data:
        out["domain_status"] = data["domainStatus"]
    else:
        raise DeserializationError("CreateDomainResponse.domain_status required")
    return out
