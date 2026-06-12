"""Generated from Smithy shape ``com.amazonaws.wellarchitected#NotificationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_upgrade_summary
    import aws_sdk_wellarchitected.types.notification_type


class NotificationSummary(TypedDict):
    type: NotRequired[
        "aws_sdk_wellarchitected.types.notification_type.NotificationType"
    ]
    """<p>The type of notification.</p>"""
    lens_upgrade_summary: NotRequired[
        "aws_sdk_wellarchitected.types.lens_upgrade_summary.LensUpgradeSummary"
    ]
    """<p>Summary of lens upgrade.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_wellarchitected.types.notification_type

        out["Type"] = aws_sdk_wellarchitected.types.notification_type.serialize_json(
            value["type"]
        )
    if "lens_upgrade_summary" in value:
        import aws_sdk_wellarchitected.types.lens_upgrade_summary

        out["LensUpgradeSummary"] = (
            aws_sdk_wellarchitected.types.lens_upgrade_summary.serialize_json(
                value["lens_upgrade_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationSummary:
    out: NotificationSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_wellarchitected.types.notification_type

        out["type"] = aws_sdk_wellarchitected.types.notification_type.deserialize_json(
            data["Type"]
        )
    if "LensUpgradeSummary" in data:
        import aws_sdk_wellarchitected.types.lens_upgrade_summary

        out["lens_upgrade_summary"] = (
            aws_sdk_wellarchitected.types.lens_upgrade_summary.deserialize_json(
                data["LensUpgradeSummary"]
            )
        )
    return out
