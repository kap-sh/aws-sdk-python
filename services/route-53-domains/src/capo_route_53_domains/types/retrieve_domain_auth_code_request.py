"""Generated from Smithy shape ``com.amazonaws.route53domains#RetrieveDomainAuthCodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name


class RetrieveDomainAuthCodeRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to get an authorization code for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveDomainAuthCodeRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveDomainAuthCodeRequest:
    out: RetrieveDomainAuthCodeRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("RetrieveDomainAuthCodeRequest.domain_name required")
    return out
