"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.sla_name
    import aws_sdk_connectcases.types.sla_status


class SlaFilter(TypedDict):
    name: NotRequired["aws_sdk_connectcases.types.sla_name.SlaName"]
    """<p>Name of an SLA.</p>"""
    status: NotRequired["aws_sdk_connectcases.types.sla_status.SlaStatus"]
    """<p>Status of an SLA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> SlaFilter:
    out: SlaFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
