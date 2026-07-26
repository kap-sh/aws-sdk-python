"""Generated from Smithy shape ``com.amazonaws.codedeploy#LifecycleEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.diagnostics
    import capo_codedeploy.types.lifecycle_event_name
    import capo_codedeploy.types.lifecycle_event_status
    import capo_codedeploy.types.timestamp


class LifecycleEvent(TypedDict, closed=True):
    lifecycle_event_name: NotRequired[
        "capo_codedeploy.types.lifecycle_event_name.LifecycleEventName"
    ]
    """<p>The deployment lifecycle event name, such as <code>ApplicationStop</code>, <code>BeforeInstall</code>, <code>AfterInstall</code>, <code>ApplicationStart</code>, or <code>ValidateService</code>.</p>"""
    diagnostics: NotRequired["capo_codedeploy.types.diagnostics.Diagnostics"]
    """<p>Diagnostic information about the deployment lifecycle event.</p>"""
    start_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment lifecycle event started.</p>"""
    end_time: NotRequired["capo_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the deployment lifecycle event ended.</p>"""
    status: NotRequired[
        "capo_codedeploy.types.lifecycle_event_status.LifecycleEventStatus"
    ]
    """<p>The deployment lifecycle event status:</p> <ul> <li> <p>Pending: The deployment lifecycle event is pending.</p> </li> <li> <p>InProgress: The deployment lifecycle event is in progress.</p> </li> <li> <p>Succeeded: The deployment lifecycle event ran successfully.</p> </li> <li> <p>Failed: The deployment lifecycle event has failed.</p> </li> <li> <p>Skipped: The deployment lifecycle event has been skipped.</p> </li> <li> <p>Unknown: The deployment lifecycle event is unknown.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleEvent) -> dict:
    out: dict = {}
    if "lifecycle_event_name" in value:
        out["lifecycleEventName"] = value["lifecycle_event_name"]
    if "diagnostics" in value:
        import capo_codedeploy.types.diagnostics

        out["diagnostics"] = capo_codedeploy.types.diagnostics.serialize_aws_json_1_1(
            value["diagnostics"]
        )
    if "start_time" in value:
        import capo_codedeploy.types.timestamp

        out["startTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codedeploy.types.timestamp

        out["endTime"] = capo_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = (
            capo_codedeploy.types.lifecycle_event_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecycleEvent:
    out: LifecycleEvent = {}  # type: ignore[typeddict-item]
    if "lifecycleEventName" in data:
        out["lifecycle_event_name"] = data["lifecycleEventName"]
    if "diagnostics" in data:
        import capo_codedeploy.types.diagnostics

        out["diagnostics"] = capo_codedeploy.types.diagnostics.deserialize_aws_json_1_1(
            data["diagnostics"]
        )
    if "startTime" in data:
        import capo_codedeploy.types.timestamp

        out["start_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_codedeploy.types.timestamp

        out["end_time"] = capo_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "status" in data:
        import capo_codedeploy.types.lifecycle_event_status

        out["status"] = (
            capo_codedeploy.types.lifecycle_event_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
