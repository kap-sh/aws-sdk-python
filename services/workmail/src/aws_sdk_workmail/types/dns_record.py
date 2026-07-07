"""Generated from Smithy shape ``com.amazonaws.workmail#DnsRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class DnsRecord(TypedDict, closed=True):
    type: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The RFC 1035 record type. Possible values: <code>CNAME</code>, <code>A</code>, <code>MX</code>.</p>"""
    hostname: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The DNS hostname.- For example, <code>domain.example.com</code>.</p>"""
    value: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The value returned by the DNS for a query to that hostname and record type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecord) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsRecord:
    out: DnsRecord = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
