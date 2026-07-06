"""Generated from Smithy shape ``com.amazonaws.connectcases#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_arn
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.domain_name


class DomainSummary(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the domain.</p>"""
    domain_arn: "aws_sdk_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain.</p>"""
    name: "aws_sdk_connectcases.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DomainSummary.domain_id required")
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError("DomainSummary.domain_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DomainSummary.name required")
    return out
