"""Generated from Smithy shape ``com.amazonaws.route53domains#PushDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.label


class PushDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p> Name of the domain. </p>"""
    target: "aws_sdk_route_53_domains.types.label.Label"
    """<p> New IPS tag for the domain. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PushDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PushDomainRequest:
    out: PushDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("PushDomainRequest.domain_name required")
    if "Target" in data:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("PushDomainRequest.target required")
    return out
