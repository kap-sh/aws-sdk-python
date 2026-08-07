"""Generated from Smithy shape ``com.amazonaws.autoscaling#ActivitiesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.activities
    import capo_auto_scaling.types.xml_string


class ActivitiesType(TypedDict, closed=True):
    activities: NotRequired["capo_auto_scaling.types.activities.Activities"]
    """<p>The scaling activities. Activities are sorted by start time. Activities still in progress are described first.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivitiesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "activities" in value:
        import capo_auto_scaling.types.activities

        capo_auto_scaling.types.activities.serialize_query(
            value["activities"], pairs, f"{key_prefix}Activities"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ActivitiesType:
    out: ActivitiesType = {}  # type: ignore[typeddict-item]
    child_activities = el.find("Activities")
    if child_activities is not None:
        import capo_auto_scaling.types.activities

        out["activities"] = capo_auto_scaling.types.activities.deserialize_query(
            child_activities
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
