"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomain``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.dns_record
    import aws_sdk_amplify.types.sub_domain_setting
    import aws_sdk_amplify.types.verified


class SubDomain(TypedDict):
    sub_domain_setting: "aws_sdk_amplify.types.sub_domain_setting.SubDomainSetting"
    """<p> Describes the settings for the subdomain. </p>"""
    verified: "aws_sdk_amplify.types.verified.Verified"
    """<p> The verified status of the subdomain </p>"""
    dns_record: "aws_sdk_amplify.types.dns_record.DNSRecord"
    """<p> The DNS record for the subdomain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubDomain) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.sub_domain_setting

    out["subDomainSetting"] = aws_sdk_amplify.types.sub_domain_setting.serialize_json(
        value["sub_domain_setting"]
    )
    out["verified"] = value["verified"]
    out["dnsRecord"] = value["dns_record"]
    return out


def deserialize_json(data: dict) -> SubDomain:
    out: SubDomain = {}  # type: ignore[typeddict-item]
    if "subDomainSetting" in data:
        import aws_sdk_amplify.types.sub_domain_setting

        out["sub_domain_setting"] = (
            aws_sdk_amplify.types.sub_domain_setting.deserialize_json(
                data["subDomainSetting"]
            )
        )
    else:
        raise DeserializationError("SubDomain.sub_domain_setting required")
    if "verified" in data:
        out["verified"] = data["verified"]
    else:
        raise DeserializationError("SubDomain.verified required")
    if "dnsRecord" in data:
        out["dns_record"] = data["dnsRecord"]
    else:
        raise DeserializationError("SubDomain.dns_record required")
    return out
