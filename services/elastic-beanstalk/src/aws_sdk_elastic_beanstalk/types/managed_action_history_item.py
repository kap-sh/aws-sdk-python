"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ManagedActionHistoryItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.action_history_status
    import aws_sdk_elastic_beanstalk.types.action_type
    import aws_sdk_elastic_beanstalk.types.failure_type
    import aws_sdk_elastic_beanstalk.types.string
    import aws_sdk_elastic_beanstalk.types.timestamp


class ManagedActionHistoryItem(TypedDict):
    action_id: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>A unique identifier for the managed action.</p>"""
    action_type: NotRequired["aws_sdk_elastic_beanstalk.types.action_type.ActionType"]
    """<p>The type of the managed action.</p>"""
    action_description: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>A description of the managed action.</p>"""
    failure_type: NotRequired[
        "aws_sdk_elastic_beanstalk.types.failure_type.FailureType"
    ]
    """<p>If the action failed, the type of failure.</p>"""
    status: NotRequired[
        "aws_sdk_elastic_beanstalk.types.action_history_status.ActionHistoryStatus"
    ]
    """<p>The status of the action.</p>"""
    failure_description: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>If the action failed, a description of the failure.</p>"""
    executed_time: NotRequired["aws_sdk_elastic_beanstalk.types.timestamp.Timestamp"]
    """<p>The date and time that the action started executing.</p>"""
    finished_time: NotRequired["aws_sdk_elastic_beanstalk.types.timestamp.Timestamp"]
    """<p>The date and time that the action finished executing.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedActionHistoryItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "action_id" in value:
        pairs.append((f"{prefix}.ActionId", str(value["action_id"])))
    if "action_type" in value:
        import aws_sdk_elastic_beanstalk.types.action_type

        aws_sdk_elastic_beanstalk.types.action_type.serialize_query(
            value["action_type"], pairs, f"{prefix}.ActionType"
        )
    if "action_description" in value:
        pairs.append((f"{prefix}.ActionDescription", str(value["action_description"])))
    if "failure_type" in value:
        import aws_sdk_elastic_beanstalk.types.failure_type

        aws_sdk_elastic_beanstalk.types.failure_type.serialize_query(
            value["failure_type"], pairs, f"{prefix}.FailureType"
        )
    if "status" in value:
        import aws_sdk_elastic_beanstalk.types.action_history_status

        aws_sdk_elastic_beanstalk.types.action_history_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "failure_description" in value:
        pairs.append(
            (f"{prefix}.FailureDescription", str(value["failure_description"]))
        )
    if "executed_time" in value:
        import aws_sdk_elastic_beanstalk.types.timestamp

        aws_sdk_elastic_beanstalk.types.timestamp.serialize_query(
            value["executed_time"], pairs, f"{prefix}.ExecutedTime"
        )
    if "finished_time" in value:
        import aws_sdk_elastic_beanstalk.types.timestamp

        aws_sdk_elastic_beanstalk.types.timestamp.serialize_query(
            value["finished_time"], pairs, f"{prefix}.FinishedTime"
        )


def deserialize_query(el: Element) -> ManagedActionHistoryItem:
    out: ManagedActionHistoryItem = {}  # type: ignore[typeddict-item]
    child_action_id = el.find("ActionId")
    if child_action_id is not None:
        out["action_id"] = str(child_action_id.text or "")
    child_action_type = el.find("ActionType")
    if child_action_type is not None:
        import aws_sdk_elastic_beanstalk.types.action_type

        out["action_type"] = (
            aws_sdk_elastic_beanstalk.types.action_type.deserialize_query(
                child_action_type
            )
        )
    child_action_description = el.find("ActionDescription")
    if child_action_description is not None:
        out["action_description"] = str(child_action_description.text or "")
    child_failure_type = el.find("FailureType")
    if child_failure_type is not None:
        import aws_sdk_elastic_beanstalk.types.failure_type

        out["failure_type"] = (
            aws_sdk_elastic_beanstalk.types.failure_type.deserialize_query(
                child_failure_type
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_elastic_beanstalk.types.action_history_status

        out["status"] = (
            aws_sdk_elastic_beanstalk.types.action_history_status.deserialize_query(
                child_status
            )
        )
    child_failure_description = el.find("FailureDescription")
    if child_failure_description is not None:
        out["failure_description"] = str(child_failure_description.text or "")
    child_executed_time = el.find("ExecutedTime")
    if child_executed_time is not None:
        import aws_sdk_elastic_beanstalk.types.timestamp

        out["executed_time"] = (
            aws_sdk_elastic_beanstalk.types.timestamp.deserialize_query(
                child_executed_time
            )
        )
    child_finished_time = el.find("FinishedTime")
    if child_finished_time is not None:
        import aws_sdk_elastic_beanstalk.types.timestamp

        out["finished_time"] = (
            aws_sdk_elastic_beanstalk.types.timestamp.deserialize_query(
                child_finished_time
            )
        )
    return out
