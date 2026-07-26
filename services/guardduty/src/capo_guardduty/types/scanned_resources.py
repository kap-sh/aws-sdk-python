"""Generated from Smithy shape ``com.amazonaws.guardduty#ScannedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.scanned_resource

ScannedResources: TypeAlias = list[
    "capo_guardduty.types.scanned_resource.ScannedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScannedResources) -> list:
    import capo_guardduty.types.scanned_resource

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.scanned_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScannedResources:
    import capo_guardduty.types.scanned_resource

    out: ScannedResources = []
    for item in data:
        out.append(capo_guardduty.types.scanned_resource.deserialize_json(item))
    return out
