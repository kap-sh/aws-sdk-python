"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewPayloadFieldAllowedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_payload_field_value


class ActionReviewPayloadFieldAllowedValue(TypedDict, closed=True):
    value: NotRequired[
        "capo_qbusiness.types.action_payload_field_value.ActionPayloadFieldValue"
    ]
    """<p>The field value.</p>"""
    display_value: NotRequired[
        "capo_qbusiness.types.action_payload_field_value.ActionPayloadFieldValue"
    ]
    """<p>The name of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionReviewPayloadFieldAllowedValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "display_value" in value:
        out["displayValue"] = value["display_value"]
    return out


def deserialize_json(data: dict) -> ActionReviewPayloadFieldAllowedValue:
    out: ActionReviewPayloadFieldAllowedValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "displayValue" in data:
        out["display_value"] = data["displayValue"]
    return out
