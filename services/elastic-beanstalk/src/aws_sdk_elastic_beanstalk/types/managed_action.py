"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ManagedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.action_status
    import aws_sdk_elastic_beanstalk.types.action_type
    import aws_sdk_elastic_beanstalk.types.string
    import aws_sdk_elastic_beanstalk.types.timestamp


class ManagedAction(TypedDict, closed=True):
    action_id: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>A unique identifier for the managed action.</p>"""
    action_description: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>A description of the managed action.</p>"""
    action_type: NotRequired["aws_sdk_elastic_beanstalk.types.action_type.ActionType"]
    """<p>The type of managed action.</p>"""
    status: NotRequired["aws_sdk_elastic_beanstalk.types.action_status.ActionStatus"]
    """<p>The status of the managed action. If the action is <code>Scheduled</code>, you can apply it immediately with <a>ApplyEnvironmentManagedAction</a>.</p>"""
    window_start_time: NotRequired[
        "aws_sdk_elastic_beanstalk.types.timestamp.Timestamp"
    ]
    """<p>The start time of the maintenance window in which the managed action will execute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action_id" in value:
        pairs.append((f"{prefix}.ActionId", str(value["action_id"])))
    if "action_description" in value:
        pairs.append((f"{prefix}.ActionDescription", str(value["action_description"])))
    if "action_type" in value:
        import aws_sdk_elastic_beanstalk.types.action_type

        aws_sdk_elastic_beanstalk.types.action_type.serialize_query(
            value["action_type"], pairs, f"{prefix}.ActionType"
        )
    if "status" in value:
        import aws_sdk_elastic_beanstalk.types.action_status

        aws_sdk_elastic_beanstalk.types.action_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "window_start_time" in value:
        import aws_sdk_elastic_beanstalk.types.timestamp

        aws_sdk_elastic_beanstalk.types.timestamp.serialize_query(
            value["window_start_time"], pairs, f"{prefix}.WindowStartTime"
        )


def deserialize_query(el: Element) -> ManagedAction:
    out: ManagedAction = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_action_description = el.find("ActionDescription")
    if child_action_description is not None:
        out["action_description"] = str(child_action_description.text or "")
    child_action_type = el.find("ActionType")
    if child_action_type is not None:
        import aws_sdk_elastic_beanstalk.types.action_type

        out["action_type"] = (
            aws_sdk_elastic_beanstalk.types.action_type.deserialize_query(
                child_action_type
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_elastic_beanstalk.types.action_status

        out["status"] = aws_sdk_elastic_beanstalk.types.action_status.deserialize_query(
            child_status
        )
    child_window_start_time = el.find("WindowStartTime")
    if child_window_start_time is not None:
        import aws_sdk_elastic_beanstalk.types.timestamp

        out["window_start_time"] = (
            aws_sdk_elastic_beanstalk.types.timestamp.deserialize_query(
                child_window_start_time
            )
        )
    return out
