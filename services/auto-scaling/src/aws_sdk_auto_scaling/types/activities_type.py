"""Generated from Smithy shape ``com.amazonaws.autoscaling#ActivitiesType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.activities
    import aws_sdk_auto_scaling.types.xml_string


class ActivitiesType(TypedDict):
    activities: NotRequired["aws_sdk_auto_scaling.types.activities.Activities"]
    """<p>The scaling activities. Activities are sorted by start time. Activities still in progress are described first.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivitiesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "activities" in value:
        import aws_sdk_auto_scaling.types.activities

        aws_sdk_auto_scaling.types.activities.serialize_query(
            value["activities"], pairs, f"{prefix}.Activities"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ActivitiesType:
    out: ActivitiesType = {}  # type: ignore[typeddict-item]
    child_activities = el.find("Activities")
    if child_activities is not None:
        import aws_sdk_auto_scaling.types.activities

        out["activities"] = aws_sdk_auto_scaling.types.activities.deserialize_query(
            child_activities
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
