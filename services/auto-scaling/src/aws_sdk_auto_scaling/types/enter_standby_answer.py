"""Generated from Smithy shape ``com.amazonaws.autoscaling#EnterStandbyAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.activities


class EnterStandbyAnswer(TypedDict, closed=True):
    activities: NotRequired["aws_sdk_auto_scaling.types.activities.Activities"]
    """<p>The activities related to moving instances into <code>Standby</code> mode.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnterStandbyAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "activities" in value:
        import aws_sdk_auto_scaling.types.activities

        aws_sdk_auto_scaling.types.activities.serialize_query(
            value["activities"], pairs, f"{prefix}.Activities"
        )


def deserialize_query(el: Element) -> EnterStandbyAnswer:
    out: EnterStandbyAnswer = {}  # type: ignore[typeddict-item]
    child_activities = el.find("Activities")
    if child_activities is not None:
        import aws_sdk_auto_scaling.types.activities

        out["activities"] = aws_sdk_auto_scaling.types.activities.deserialize_query(
            child_activities
        )
    return out
