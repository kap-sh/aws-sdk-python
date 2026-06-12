"""Generated from Smithy shape ``com.amazonaws.route53domains#CancelDomainTransferToAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name


class CancelDomainTransferToAnotherAwsAccountRequest(TypedDict):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain for which you want to cancel the transfer to another Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDomainTransferToAnotherAwsAccountRequest,
) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDomainTransferToAnotherAwsAccountRequest:
    out: CancelDomainTransferToAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "CancelDomainTransferToAnotherAwsAccountRequest.domain_name required"
        )
    return out
