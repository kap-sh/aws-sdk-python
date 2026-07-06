"""Generated from Smithy shape ``com.amazonaws.pinpointemail#InboxPlacementTrackingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.enabled
    import aws_sdk_pinpoint_email.types.isp_name_list

InboxPlacementTrackingOption = TypedDict(
    "InboxPlacementTrackingOption",
    {
        "global": "aws_sdk_pinpoint_email.types.enabled.Enabled",
        "tracked_isps": NotRequired[
            "aws_sdk_pinpoint_email.types.isp_name_list.IspNameList"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: InboxPlacementTrackingOption) -> dict:
    out: dict = {}
    out["Global"] = value.get("global", False)
    if "tracked_isps" in value:
        import aws_sdk_pinpoint_email.types.isp_name_list

        out["TrackedIsps"] = aws_sdk_pinpoint_email.types.isp_name_list.serialize_json(
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
        import aws_sdk_pinpoint_email.types.isp_name_list

        out["tracked_isps"] = (
            aws_sdk_pinpoint_email.types.isp_name_list.deserialize_json(
                data["TrackedIsps"]
            )
        )
    return out
