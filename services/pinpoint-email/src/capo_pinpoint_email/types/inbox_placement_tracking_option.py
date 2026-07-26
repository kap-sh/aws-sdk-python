"""Generated from Smithy shape ``com.amazonaws.pinpointemail#InboxPlacementTrackingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.isp_name_list

InboxPlacementTrackingOption = TypedDict(
    "InboxPlacementTrackingOption",
    {
        "global": "capo_pinpoint_email.types.enabled.Enabled",
        "tracked_isps": NotRequired[
            "capo_pinpoint_email.types.isp_name_list.IspNameList"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: InboxPlacementTrackingOption) -> dict:
    out: dict = {}
    out["Global"] = value.get("global", False)
    if "tracked_isps" in value:
        import capo_pinpoint_email.types.isp_name_list

        out["TrackedIsps"] = capo_pinpoint_email.types.isp_name_list.serialize_json(
            value["tracked_isps"]
        )
    return out


def deserialize_json(data: dict) -> InboxPlacementTrackingOption:
    out: InboxPlacementTrackingOption = {}  # type: ignore[typeddict-item]
    if "Global" in data:
        out["global"] = data["Global"]
    else:
        out["global"] = False
    if "TrackedIsps" in data:
        import capo_pinpoint_email.types.isp_name_list

        out["tracked_isps"] = capo_pinpoint_email.types.isp_name_list.deserialize_json(
            data["TrackedIsps"]
        )
    return out
