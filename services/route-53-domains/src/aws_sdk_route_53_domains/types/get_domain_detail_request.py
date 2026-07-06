"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainDetailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name


class GetDomainDetailRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to get detailed information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainDetailRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainDetailRequest:
    out: GetDomainDetailRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("GetDomainDetailRequest.domain_name required")
    return out
