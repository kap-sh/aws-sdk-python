"""Generated from Smithy shape ``com.amazonaws.securityagent#DnsVerification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.dns_record_type


class DnsVerification(TypedDict, closed=True):
    token: NotRequired["str"]
    """<p>The verification token to include in the DNS record value.</p>"""
    dns_record_name: NotRequired["str"]
    """<p>The name of the DNS record to create for verification.</p>"""
    dns_record_type: NotRequired[
        "aws_sdk_securityagent.types.dns_record_type.DNSRecordType"
    ]
    """<p>The type of DNS record to create. Currently, only TXT is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DnsVerification) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "dns_record_name" in value:
        out["dnsRecordName"] = value["dns_record_name"]
    if "dns_record_type" in value:
        import aws_sdk_securityagent.types.dns_record_type

        out["dnsRecordType"] = (
            aws_sdk_securityagent.types.dns_record_type.serialize_json(
                value["dns_record_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DnsVerification:
    out: DnsVerification = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    if "dnsRecordName" in data:
        out["dns_record_name"] = data["dnsRecordName"]
    if "dnsRecordType" in data:
        import aws_sdk_securityagent.types.dns_record_type

        out["dns_record_type"] = (
            aws_sdk_securityagent.types.dns_record_type.deserialize_json(
                data["dnsRecordType"]
            )
        )
    return out
