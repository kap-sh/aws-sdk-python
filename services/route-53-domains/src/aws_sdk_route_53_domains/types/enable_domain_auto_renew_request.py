"""Generated from Smithy shape ``com.amazonaws.route53domains#EnableDomainAutoRenewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name


class EnableDomainAutoRenewRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to enable automatic renewal for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableDomainAutoRenewRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableDomainAutoRenewRequest:
    out: EnableDomainAutoRenewRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("EnableDomainAutoRenewRequest.domain_name required")
    return out
