"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#R53ResourceRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class R53ResourceRecord(TypedDict):
    domain_name: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The DNS target domain name.</p>"""
    record_set_id: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The Route 53 Resource Record Set ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: R53ResourceRecord) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "record_set_id" in value:
        out["recordSetId"] = value["record_set_id"]
    return out


def deserialize_json(data: dict) -> R53ResourceRecord:
    out: R53ResourceRecord = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "recordSetId" in data:
        out["record_set_id"] = data["recordSetId"]
    return out
