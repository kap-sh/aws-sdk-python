"""Generated from Smithy shape ``com.amazonaws.lightsail#PendingMaintenanceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string


class PendingMaintenanceAction(TypedDict, closed=True):
    action: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The type of pending database maintenance action.</p>"""
    description: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Additional detail about the pending database maintenance action.</p>"""
    current_apply_date: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The effective date of the pending database maintenance action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingMaintenanceAction) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "description" in value:
        out["description"] = value["description"]
    if "current_apply_date" in value:
        import aws_sdk_lightsail.types.iso_date

        out["currentApplyDate"] = (
            aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
                value["current_apply_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingMaintenanceAction:
    out: PendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    if "description" in data:
        out["description"] = data["description"]
    if "currentApplyDate" in data:
        import aws_sdk_lightsail.types.iso_date

        out["current_apply_date"] = (
            aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
                data["currentApplyDate"]
            )
        )
    return out
