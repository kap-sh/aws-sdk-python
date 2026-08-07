"""Generated from Smithy shape ``com.amazonaws.autoscaling#ActivityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.activity


class ActivityType(TypedDict, closed=True):
    activity: NotRequired["capo_auto_scaling.types.activity.Activity"]
    """<p>A scaling activity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "activity" in value:
        import capo_auto_scaling.types.activity

        capo_auto_scaling.types.activity.serialize_query(
            value["activity"], pairs, f"{key_prefix}Activity"
        )


def deserialize_query(el: Element) -> ActivityType:
    out: ActivityType = {}  # type: ignore[typeddict-item]
    child_activity = el.find("Activity")
    if child_activity is not None:
        import capo_auto_scaling.types.activity

        out["activity"] = capo_auto_scaling.types.activity.deserialize_query(
            child_activity
        )
    return out
