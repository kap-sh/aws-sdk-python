"""Generated from Smithy shape ``com.amazonaws.route53domains#AssociateDelegationSignerToDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.dnssec_signing_attributes
    import aws_sdk_route_53_domains.types.domain_name


class AssociateDelegationSignerToDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    signing_attributes: "aws_sdk_route_53_domains.types.dnssec_signing_attributes.DnssecSigningAttributes"
    """<p>The information about a key, including the algorithm, public key-value, and flags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDelegationSignerToDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import aws_sdk_route_53_domains.types.dnssec_signing_attributes

    out["SigningAttributes"] = (
        aws_sdk_route_53_domains.types.dnssec_signing_attributes.serialize_aws_json_1_1(
            value["signing_attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDelegationSignerToDomainRequest:
    out: AssociateDelegationSignerToDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "AssociateDelegationSignerToDomainRequest.domain_name required"
        )
    if "SigningAttributes" in data:
        import aws_sdk_route_53_domains.types.dnssec_signing_attributes

        out["signing_attributes"] = (
            aws_sdk_route_53_domains.types.dnssec_signing_attributes.deserialize_aws_json_1_1(
                data["SigningAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateDelegationSignerToDomainRequest.signing_attributes required"
        )
    return out
