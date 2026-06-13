"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.dedupe_string
    import aws_sdk_ssm_incidents.types.impact
    import aws_sdk_ssm_incidents.types.incident_summary
    import aws_sdk_ssm_incidents.types.incident_title
    import aws_sdk_ssm_incidents.types.notification_target_set
    import aws_sdk_ssm_incidents.types.tag_map


class IncidentTemplate(TypedDict):
    title: "aws_sdk_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident. </p>"""
    impact: "aws_sdk_ssm_incidents.types.impact.Impact"
    """<p>The impact of the incident on your customers and applications.</p> <p class=\"title\"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    summary: NotRequired["aws_sdk_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context.</p>"""
    dedupe_string: NotRequired["aws_sdk_ssm_incidents.types.dedupe_string.DedupeString"]
    """<p>The string Incident Manager uses to prevent the same root cause from creating multiple incidents in the same account.</p> <p>A deduplication string is a term or phrase the system uses to check for duplicate incidents. If you specify a deduplication string, Incident Manager searches for open incidents that contain the same string in the <code>dedupeString</code> field when it creates the incident. If a duplicate is detected, Incident Manager deduplicates the newer incident into the existing incident.</p> <note> <p>By default, Incident Manager automatically deduplicates multiple incidents created by the same Amazon CloudWatch alarm or Amazon EventBridge event. You don't have to enter your own deduplication string to prevent duplication for these resource types.</p> </note>"""
    notification_targets: NotRequired[
        "aws_sdk_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""
    incident_tags: NotRequired["aws_sdk_ssm_incidents.types.tag_map.TagMap"]
    """<p>Tags to assign to the template. When the <code>StartIncident</code> API action is called, Incident Manager assigns the tags specified in the template to the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentTemplate) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["impact"] = value["impact"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "dedupe_string" in value:
        out["dedupeString"] = value["dedupe_string"]
    if "notification_targets" in value:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["notificationTargets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.serialize_json(
                value["notification_targets"]
            )
        )
    if "incident_tags" in value:
        import aws_sdk_ssm_incidents.types.tag_map

        out["incidentTags"] = aws_sdk_ssm_incidents.types.tag_map.serialize_json(
            value["incident_tags"]
        )
    return out


def deserialize_json(data: dict) -> IncidentTemplate:
    out: IncidentTemplate = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("IncidentTemplate.title required")
    if "impact" in data:
        out["impact"] = data["impact"]
    else:
        raise DeserializationError("IncidentTemplate.impact required")
    if "summary" in data:
        out["summary"] = data["summary"]
    if "dedupeString" in data:
        out["dedupe_string"] = data["dedupeString"]
    if "notificationTargets" in data:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["notification_targets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.deserialize_json(
                data["notificationTargets"]
            )
        )
    if "incidentTags" in data:
        import aws_sdk_ssm_incidents.types.tag_map

        out["incident_tags"] = aws_sdk_ssm_incidents.types.tag_map.deserialize_json(
            data["incidentTags"]
        )
    return out
