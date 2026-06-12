"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.scheduled_action_list
    import aws_sdk_redshift.types.string


class ScheduledActionsMessage(TypedDict):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeScheduledActions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    scheduled_actions: NotRequired[
        "aws_sdk_redshift.types.scheduled_action_list.ScheduledActionList"
    ]
    """<p>List of retrieved scheduled actions. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "scheduled_actions" in value:
        import aws_sdk_redshift.types.scheduled_action_list

        aws_sdk_redshift.types.scheduled_action_list.serialize_query(
            value["scheduled_actions"], pairs, f"{prefix}.ScheduledActions"
        )


def deserialize_query(el: Element) -> ScheduledActionsMessage:
    out: ScheduledActionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_scheduled_actions = el.find("ScheduledActions")
    if child_scheduled_actions is not None:
        import aws_sdk_redshift.types.scheduled_action_list

        out["scheduled_actions"] = (
            aws_sdk_redshift.types.scheduled_action_list.deserialize_query(
                child_scheduled_actions
            )
        )
    return out
