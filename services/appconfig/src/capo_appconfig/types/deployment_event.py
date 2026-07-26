"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.action_invocations
    import capo_appconfig.types.deployment_event_type
    import capo_appconfig.types.description
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.triggered_by


class DeploymentEvent(TypedDict, closed=True):
    event_type: NotRequired[
        "capo_appconfig.types.deployment_event_type.DeploymentEventType"
    ]
    """<p>The type of deployment event. Deployment event types include the start, stop, or completion of a deployment; a percentage update; the start or stop of a bake period; and the start or completion of a rollback.</p>"""
    triggered_by: NotRequired["capo_appconfig.types.triggered_by.TriggeredBy"]
    """<p>The entity that triggered the deployment event. Events can be triggered by a user, AppConfig, an Amazon CloudWatch alarm, or an internal error.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the deployment event. Descriptions include, but are not limited to, the following:</p> <ul> <li> <p>The Amazon Web Services account or the Amazon CloudWatch alarm ARN that initiated a rollback.</p> </li> <li> <p>The percentage of hosts that received the deployment.</p> </li> <li> <p>A recommendation to attempt a new deployment (in the case of an internal error).</p> </li> </ul>"""
    action_invocations: NotRequired[
        "capo_appconfig.types.action_invocations.ActionInvocations"
    ]
    """<p>The list of extensions that were invoked as part of the deployment.</p>"""
    occurred_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the event occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentEvent) -> dict:
    out: dict = {}
    if "event_type" in value:
        import capo_appconfig.types.deployment_event_type

        out["EventType"] = capo_appconfig.types.deployment_event_type.serialize_json(
            value["event_type"]
        )
    if "triggered_by" in value:
        import capo_appconfig.types.triggered_by

        out["TriggeredBy"] = capo_appconfig.types.triggered_by.serialize_json(
            value["triggered_by"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "action_invocations" in value:
        import capo_appconfig.types.action_invocations

        out["ActionInvocations"] = (
            capo_appconfig.types.action_invocations.serialize_json(
                value["action_invocations"]
            )
        )
    if "occurred_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["OccurredAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["occurred_at"]
        )
    return out


def deserialize_json(data: dict) -> DeploymentEvent:
    out: DeploymentEvent = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import capo_appconfig.types.deployment_event_type

        out["event_type"] = capo_appconfig.types.deployment_event_type.deserialize_json(
            data["EventType"]
        )
    if "TriggeredBy" in data:
        import capo_appconfig.types.triggered_by

        out["triggered_by"] = capo_appconfig.types.triggered_by.deserialize_json(
            data["TriggeredBy"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ActionInvocations" in data:
        import capo_appconfig.types.action_invocations

        out["action_invocations"] = (
            capo_appconfig.types.action_invocations.deserialize_json(
                data["ActionInvocations"]
            )
        )
    if "OccurredAt" in data:
        import capo_appconfig.types.iso8601_date_time

        out["occurred_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["OccurredAt"]
        )
    return out
