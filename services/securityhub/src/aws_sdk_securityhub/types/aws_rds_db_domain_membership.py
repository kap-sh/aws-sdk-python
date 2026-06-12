"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbDomainMembership``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbDomainMembership(TypedDict):
    domain: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Active Directory domain.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the Active Directory Domain membership for the DB instance.</p>"""
    fqdn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The fully qualified domain name of the Active Directory domain.</p>"""
    iam_role_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbDomainMembership) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "status" in value:
        out["Status"] = value["status"]
    if "fqdn" in value:
        out["Fqdn"] = value["fqdn"]
    if "iam_role_name" in value:
        out["IamRoleName"] = value["iam_role_name"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbDomainMembership:
    out: AwsRdsDbDomainMembership = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Fqdn" in data:
        out["fqdn"] = data["Fqdn"]
    if "IamRoleName" in data:
        out["iam_role_name"] = data["IamRoleName"]
    return out
