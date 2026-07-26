"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlInsightsMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_insights_metadata_item

ControlInsightsMetadata: TypeAlias = list[
    "capo_auditmanager.types.control_insights_metadata_item.ControlInsightsMetadataItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlInsightsMetadata) -> list:
    import capo_auditmanager.types.control_insights_metadata_item

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.control_insights_metadata_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ControlInsightsMetadata:
    import capo_auditmanager.types.control_insights_metadata_item

    out: ControlInsightsMetadata = []
    for item in data:
        out.append(
            capo_auditmanager.types.control_insights_metadata_item.deserialize_json(
                item
            )
        )
    return out
