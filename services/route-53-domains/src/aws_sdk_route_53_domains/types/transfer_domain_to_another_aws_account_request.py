"""Generated from Smithy shape ``com.amazonaws.route53domains#TransferDomainToAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.account_id
    import aws_sdk_route_53_domains.types.domain_name


class TransferDomainToAnotherAwsAccountRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to transfer from the current Amazon Web Services account to another account.</p>"""
    account_id: "aws_sdk_route_53_domains.types.account_id.AccountId"
    """<p>The account ID of the Amazon Web Services account that you want to transfer the domain to, for example, <code>111122223333</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferDomainToAnotherAwsAccountRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransferDomainToAnotherAwsAccountRequest:
    out: TransferDomainToAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "TransferDomainToAnotherAwsAccountRequest.domain_name required"
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "TransferDomainToAnotherAwsAccountRequest.account_id required"
        )
    return out
