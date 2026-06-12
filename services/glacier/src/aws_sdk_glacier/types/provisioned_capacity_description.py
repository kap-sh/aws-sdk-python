"""Generated from Smithy shape ``com.amazonaws.glacier#ProvisionedCapacityDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ProvisionedCapacityDescription(TypedDict):
    capacity_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The ID that identifies the provisioned capacity unit.</p>"""
    start_date: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The date that the provisioned capacity unit was purchased, in Universal Coordinated Time (UTC).</p>"""
    expiration_date: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The date that the provisioned capacity unit expires, in Universal Coordinated Time (UTC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedCapacityDescription) -> dict:
    out: dict = {}
    if "capacity_id" in value:
        out["CapacityId"] = value["capacity_id"]
    if "start_date" in value:
        out["StartDate"] = value["start_date"]
    if "expiration_date" in value:
        out["ExpirationDate"] = value["expiration_date"]
    return out


def deserialize_json(data: dict) -> ProvisionedCapacityDescription:
    out: ProvisionedCapacityDescription = {}  # type: ignore[typeddict-item]
    if "CapacityId" in data:
        out["capacity_id"] = data["CapacityId"]
    if "StartDate" in data:
        out["start_date"] = data["StartDate"]
    if "ExpirationDate" in data:
        out["expiration_date"] = data["ExpirationDate"]
    return out
