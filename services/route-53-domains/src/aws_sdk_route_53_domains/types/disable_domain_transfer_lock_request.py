"""Generated from Smithy shape ``com.amazonaws.route53domains#DisableDomainTransferLockRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name


class DisableDomainTransferLockRequest(TypedDict):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to remove the transfer lock for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableDomainTransferLockRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableDomainTransferLockRequest:
    out: DisableDomainTransferLockRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "DisableDomainTransferLockRequest.domain_name required"
        )
    return out
