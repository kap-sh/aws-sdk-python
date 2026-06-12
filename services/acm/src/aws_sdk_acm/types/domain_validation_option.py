"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidationOption``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.domain_name_string


class DomainValidationOption(TypedDict):
    domain_name: "aws_sdk_acm.types.domain_name_string.DomainNameString"
    """<p>A fully qualified domain name (FQDN) in the certificate request.</p>"""
    validation_domain: "aws_sdk_acm.types.domain_name_string.DomainNameString"
    """<p>The domain name that you want ACM to use to send you validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the <code>DomainName</code> value or a superdomain of the <code>DomainName</code> value. For example, if you request a certificate for <code>testing.example.com</code>, you can specify <code>example.com</code> for this value. In that case, ACM sends domain validation emails to the following five addresses:</p> <ul> <li> <p>admin@example.com</p> </li> <li> <p>administrator@example.com</p> </li> <li> <p>hostmaster@example.com</p> </li> <li> <p>postmaster@example.com</p> </li> <li> <p>webmaster@example.com</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationOption) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["ValidationDomain"] = value["validation_domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainValidationOption:
    out: DomainValidationOption = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DomainValidationOption.domain_name required")
    if "ValidationDomain" in data:
        out["validation_domain"] = data["ValidationDomain"]
    else:
        raise DeserializationError("DomainValidationOption.validation_domain required")
    return out
