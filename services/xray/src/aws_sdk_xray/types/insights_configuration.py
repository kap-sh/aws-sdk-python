"""Generated from Smithy shape ``com.amazonaws.xray#InsightsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_boolean


class InsightsConfiguration(TypedDict, closed=True):
    insights_enabled: NotRequired["aws_sdk_xray.types.nullable_boolean.NullableBoolean"]
    """<p>Set the InsightsEnabled value to true to enable insights or false to disable insights.</p>"""
    notifications_enabled: NotRequired[
        "aws_sdk_xray.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set the NotificationsEnabled value to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsConfiguration) -> dict:
    out: dict = {}
    if "insights_enabled" in value:
        out["InsightsEnabled"] = value["insights_enabled"]
    if "notifications_enabled" in value:
        out["NotificationsEnabled"] = value["notifications_enabled"]
    return out


def deserialize_json(data: dict) -> InsightsConfiguration:
    out: InsightsConfiguration = {}  # type: ignore[typeddict-item]
    if "InsightsEnabled" in data:
        out["insights_enabled"] = data["InsightsEnabled"]
    if "NotificationsEnabled" in data:
        out["notifications_enabled"] = data["NotificationsEnabled"]
    return out
