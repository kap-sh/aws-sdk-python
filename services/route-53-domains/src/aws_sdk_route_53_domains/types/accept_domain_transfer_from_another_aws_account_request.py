"""Generated from Smithy shape ``com.amazonaws.route53domains#AcceptDomainTransferFromAnotherAwsAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.password


class AcceptDomainTransferFromAnotherAwsAccountRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    r"""<p>The name of the domain that was specified when another Amazon Web Services account submitted a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\">TransferDomainToAnotherAwsAccount</a> request. </p>"""
    password: "aws_sdk_route_53_domains.types.password.Password"
    r"""<p>The password that was returned by the <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_TransferDomainToAnotherAwsAccount.html\">TransferDomainToAnotherAwsAccount</a> request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcceptDomainTransferFromAnotherAwsAccountRequest,
) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AcceptDomainTransferFromAnotherAwsAccountRequest:
    out: AcceptDomainTransferFromAnotherAwsAccountRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "AcceptDomainTransferFromAnotherAwsAccountRequest.domain_name required"
        )
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError(
            "AcceptDomainTransferFromAnotherAwsAccountRequest.password required"
        )
    return out
