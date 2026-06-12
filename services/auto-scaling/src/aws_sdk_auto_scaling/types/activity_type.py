"""Generated from Smithy shape ``com.amazonaws.autoscaling#ActivityType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.activity


class ActivityType(TypedDict):
    activity: NotRequired["aws_sdk_auto_scaling.types.activity.Activity"]
    """<p>A scaling activity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "activity" in value:
        import aws_sdk_auto_scaling.types.activity

        aws_sdk_auto_scaling.types.activity.serialize_query(
            value["activity"], pairs, f"{prefix}.Activity"
        )


def deserialize_query(el: Element) -> ActivityType:
    out: ActivityType = {}  # type: ignore[typeddict-item]
    child_activity = el.find("Activity")
    if child_activity is not None:
        import aws_sdk_auto_scaling.types.activity

        out["activity"] = aws_sdk_auto_scaling.types.activity.deserialize_query(
            child_activity
        )
    return out
