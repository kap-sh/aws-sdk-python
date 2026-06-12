"""Generated from Smithy shape ``com.amazonaws.health#Event``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.availability_zone
    import aws_sdk_health.types.event_actionability
    import aws_sdk_health.types.event_arn
    import aws_sdk_health.types.event_persona_list
    import aws_sdk_health.types.event_scope_code
    import aws_sdk_health.types.event_status_code
    import aws_sdk_health.types.event_type_category
    import aws_sdk_health.types.event_type_code
    import aws_sdk_health.types.region
    import aws_sdk_health.types.service
    import aws_sdk_health.types.timestamp


class Event(TypedDict):
    arn: NotRequired["aws_sdk_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    service: NotRequired["aws_sdk_health.types.service.service"]
    """<p>The Amazon Web Services service that is affected by the event. For example, <code>EC2</code>, <code>RDS</code>.</p>"""
    event_type_code: NotRequired["aws_sdk_health.types.event_type_code.eventTypeCode"]
    """<p>The unique identifier for the event type. The format is <code>AWS_<i>SERVICE</i>_<i>DESCRIPTION</i> </code>; for example, <code>AWS_EC2_SYSTEM_MAINTENANCE_EVENT</code>.</p>"""
    event_type_category: NotRequired[
        "aws_sdk_health.types.event_type_category.eventTypeCategory"
    ]
    """<p>A list of event type category codes. Possible values are <code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>. Currently, the <code>investigation</code> value isn't supported at this time.</p>"""
    region: NotRequired["aws_sdk_health.types.region.region"]
    """<p>The Amazon Web Services Region name of the event.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_health.types.availability_zone.availabilityZone"
    ]
    """<p>The Amazon Web Services Availability Zone of the event. For example, us-east-1a.</p>"""
    start_time: NotRequired["aws_sdk_health.types.timestamp.timestamp"]
    """<p>The date and time that the event began.</p>"""
    end_time: NotRequired["aws_sdk_health.types.timestamp.timestamp"]
    """<p>The date and time that the event ended.</p>"""
    last_updated_time: NotRequired["aws_sdk_health.types.timestamp.timestamp"]
    """<p>The most recent date and time that the event was updated.</p>"""
    status_code: NotRequired["aws_sdk_health.types.event_status_code.eventStatusCode"]
    """<p>The most recent status of the event. Possible values are <code>open</code>, <code>closed</code>, and <code>upcoming</code>.</p>"""
    event_scope_code: NotRequired[
        "aws_sdk_health.types.event_scope_code.eventScopeCode"
    ]
    """<p>This parameter specifies if the Health event is a public Amazon Web Services service event or an account-specific event.</p> <ul> <li> <p>If the <code>eventScopeCode</code> value is <code>PUBLIC</code>, then the <code>affectedAccounts</code> value is always empty.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>ACCOUNT_SPECIFIC</code>, then the <code>affectedAccounts</code> value lists the affected Amazon Web Services accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have Amazon Web Services accounts that use that service, those account IDs appear in the response.</p> </li> <li> <p>If the <code>eventScopeCode</code> value is <code>NONE</code>, then the <code>eventArn</code> that you specified in the request is invalid or doesn't exist.</p> </li> </ul>"""
    actionability: NotRequired[
        "aws_sdk_health.types.event_actionability.EventActionability"
    ]
    """<p>The actionability classification of the event. Possible values are <code>ACTION_REQUIRED</code>, <code>ACTION_MAY_BE_REQUIRED</code> and <code>INFORMATIONAL</code>. Events with <code>ACTION_REQUIRED</code> actionability require customer action to resolve or mitigate the event. Events with <code>ACTION_MAY_BE_REQUIRED</code> actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with <code>INFORMATIONAL</code> actionability are provided for awareness and do not require immediate action.</p>"""
    personas: NotRequired["aws_sdk_health.types.event_persona_list.EventPersonaList"]
    """<p>A list of persona classifications that indicate the target audience for the event. Possible values are <code>OPERATIONS</code>, <code>SECURITY</code>, and <code>BILLING</code>. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "service" in value:
        out["service"] = value["service"]
    if "event_type_code" in value:
        out["eventTypeCode"] = value["event_type_code"]
    if "event_type_category" in value:
        import aws_sdk_health.types.event_type_category

        out["eventTypeCategory"] = (
            aws_sdk_health.types.event_type_category.serialize_aws_json_1_1(
                value["event_type_category"]
            )
        )
    if "region" in value:
        out["region"] = value["region"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "start_time" in value:
        import aws_sdk_health.types.timestamp

        out["startTime"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_health.types.timestamp

        out["endTime"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_health.types.timestamp

        out["lastUpdatedTime"] = aws_sdk_health.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import aws_sdk_health.types.event_status_code

        out["statusCode"] = (
            aws_sdk_health.types.event_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "event_scope_code" in value:
        import aws_sdk_health.types.event_scope_code

        out["eventScopeCode"] = (
            aws_sdk_health.types.event_scope_code.serialize_aws_json_1_1(
                value["event_scope_code"]
            )
        )
    if "actionability" in value:
        import aws_sdk_health.types.event_actionability

        out["actionability"] = (
            aws_sdk_health.types.event_actionability.serialize_aws_json_1_1(
                value["actionability"]
            )
        )
    if "personas" in value:
        import aws_sdk_health.types.event_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_persona_list.serialize_aws_json_1_1(
                value["personas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "service" in data:
        out["service"] = data["service"]
    if "eventTypeCode" in data:
        out["event_type_code"] = data["eventTypeCode"]
    if "eventTypeCategory" in data:
        import aws_sdk_health.types.event_type_category

        out["event_type_category"] = (
            aws_sdk_health.types.event_type_category.deserialize_aws_json_1_1(
                data["eventTypeCategory"]
            )
        )
    if "region" in data:
        out["region"] = data["region"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "startTime" in data:
        import aws_sdk_health.types.timestamp

        out["start_time"] = aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_health.types.timestamp

        out["end_time"] = aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_health.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_health.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdatedTime"]
            )
        )
    if "statusCode" in data:
        import aws_sdk_health.types.event_status_code

        out["status_code"] = (
            aws_sdk_health.types.event_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "eventScopeCode" in data:
        import aws_sdk_health.types.event_scope_code

        out["event_scope_code"] = (
            aws_sdk_health.types.event_scope_code.deserialize_aws_json_1_1(
                data["eventScopeCode"]
            )
        )
    if "actionability" in data:
        import aws_sdk_health.types.event_actionability

        out["actionability"] = (
            aws_sdk_health.types.event_actionability.deserialize_aws_json_1_1(
                data["actionability"]
            )
        )
    if "personas" in data:
        import aws_sdk_health.types.event_persona_list

        out["personas"] = (
            aws_sdk_health.types.event_persona_list.deserialize_aws_json_1_1(
                data["personas"]
            )
        )
    return out
