"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteJourneyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.closed_days
    import aws_sdk_pinpoint.types.journey_channel_settings
    import aws_sdk_pinpoint.types.journey_limits
    import aws_sdk_pinpoint.types.journey_schedule
    import aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element
    import aws_sdk_pinpoint.types.map_of_activity
    import aws_sdk_pinpoint.types.open_hours
    import aws_sdk_pinpoint.types.quiet_time
    import aws_sdk_pinpoint.types.start_condition
    import aws_sdk_pinpoint.types.state


class WriteJourneyRequest(TypedDict):
    activities: NotRequired["aws_sdk_pinpoint.types.map_of_activity.MapOfActivity"]
    """<p>A map that contains a set of Activity objects, one object for each activity in the journey. For each Activity object, the key is the unique identifier (string) for an activity and the value is the settings for the activity. An activity identifier can contain a maximum of 100 characters. The characters must be alphanumeric characters.</p>"""
    creation_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the journey was created.</p>"""
    last_modified_date: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the journey was last modified.</p>"""
    limits: NotRequired["aws_sdk_pinpoint.types.journey_limits.JourneyLimits"]
    """<p>The messaging and entry limits for the journey.</p>"""
    local_time: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the journey's scheduled start and end times use each participant's local time. To base the schedule on each participant's local time, set this value to true.</p>"""
    name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the journey. A journey name can contain a maximum of 150 characters. The characters can be alphanumeric characters or symbols, such as underscores (_) or hyphens (-). A journey name can't contain any spaces.</p>"""
    quiet_time: NotRequired["aws_sdk_pinpoint.types.quiet_time.QuietTime"]
    """<p>The quiet time settings for the journey. Quiet time is a specific time range when a journey doesn't send messages to participants, if all the following conditions are met:</p> <ul><li><p>The EndpointDemographic.Timezone property of the endpoint for the participant is set to a valid value.</p></li> <li><p>The current time in the participant's time zone is later than or equal to the time specified by the QuietTime.Start property for the journey.</p></li> <li><p>The current time in the participant's time zone is earlier than or equal to the time specified by the QuietTime.End property for the journey.</p></li></ul> <p>If any of the preceding conditions isn't met, the participant will receive messages from the journey, even if quiet time is enabled.</p>"""
    refresh_frequency: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The frequency with which Amazon Pinpoint evaluates segment and event data for the journey, as a duration in ISO 8601 format.</p>"""
    schedule: NotRequired["aws_sdk_pinpoint.types.journey_schedule.JourneySchedule"]
    """<p>The schedule settings for the journey.</p>"""
    start_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the first activity in the journey. The identifier for this activity can contain a maximum of 128 characters. The characters must be alphanumeric characters.</p>"""
    start_condition: NotRequired[
        "aws_sdk_pinpoint.types.start_condition.StartCondition"
    ]
    """<p>The segment that defines which users are participants in the journey.</p>"""
    state: NotRequired["aws_sdk_pinpoint.types.state.State"]
    """<p>The status of the journey. Valid values are:</p> <ul><li><p>DRAFT - Saves the journey and doesn't publish it.</p></li> <li><p>ACTIVE - Saves and publishes the journey. Depending on the journey's schedule, the journey starts running immediately or at the scheduled start time. If a journey's status is ACTIVE, you can't add, change, or remove activities from it.</p></li></ul> <p>PAUSED, CANCELLED, COMPLETED, and CLOSED states are not supported in requests to create or update a journey. To cancel, pause, or resume a journey, use the <link linkend=\"apps-application-id-journeys-journey-id-state\">Journey State</link> resource.</p>"""
    wait_for_quiet_time: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether endpoints in quiet hours should enter a wait till the end of their quiet hours.</p>"""
    refresh_on_segment_update: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Indicates whether the journey participants should be refreshed when a segment is updated.</p>"""
    journey_channel_settings: NotRequired[
        "aws_sdk_pinpoint.types.journey_channel_settings.JourneyChannelSettings"
    ]
    """<p>The channel-specific configurations for the journey.</p>"""
    sending_schedule: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Indicates if journey has Advance Quiet Time enabled. This flag should be set to true in order to allow using OpenHours and ClosedDays.</p>"""
    open_hours: NotRequired["aws_sdk_pinpoint.types.open_hours.OpenHours"]
    """<p>The time when journey allow to send messages. QuietTime should be configured first and SendingSchedule should be set to true.</p>"""
    closed_days: NotRequired["aws_sdk_pinpoint.types.closed_days.ClosedDays"]
    """<p>The time when journey will stop sending messages. QuietTime should be configured first and SendingSchedule should be set to true.</p>"""
    timezone_estimation_methods: NotRequired[
        "aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element.ListOf__TimezoneEstimationMethodsElement"
    ]
    """<p>An array of time zone estimation methods, if any, to use for determining an <a href=\"https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id.html\">Endpoints</a> time zone if the Endpoint does not have a value for the Demographic.Timezone attribute.</p> <ul> <li><p>PHONE_NUMBER - A time zone is determined based on the Endpoint.Address and Endpoint.Location.Country.</p></li> <li><p>POSTAL_CODE - A time zone is determined based on the Endpoint.Location.PostalCode and Endpoint.Location.Country.</p> <note><p>POSTAL_CODE detection is only supported in the United States, United Kingdom, Australia, New Zealand, Canada, France, Italy, Spain, Germany and in regions where Amazon Pinpoint is available.</p></note></li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteJourneyRequest) -> dict:
    out: dict = {}
    if "activities" in value:
        import aws_sdk_pinpoint.types.map_of_activity

        out["Activities"] = aws_sdk_pinpoint.types.map_of_activity.serialize_json(
            value["activities"]
        )
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "limits" in value:
        import aws_sdk_pinpoint.types.journey_limits

        out["Limits"] = aws_sdk_pinpoint.types.journey_limits.serialize_json(
            value["limits"]
        )
    if "local_time" in value:
        out["LocalTime"] = value["local_time"]
    if "name" in value:
        out["Name"] = value["name"]
    if "quiet_time" in value:
        import aws_sdk_pinpoint.types.quiet_time

        out["QuietTime"] = aws_sdk_pinpoint.types.quiet_time.serialize_json(
            value["quiet_time"]
        )
    if "refresh_frequency" in value:
        out["RefreshFrequency"] = value["refresh_frequency"]
    if "schedule" in value:
        import aws_sdk_pinpoint.types.journey_schedule

        out["Schedule"] = aws_sdk_pinpoint.types.journey_schedule.serialize_json(
            value["schedule"]
        )
    if "start_activity" in value:
        out["StartActivity"] = value["start_activity"]
    if "start_condition" in value:
        import aws_sdk_pinpoint.types.start_condition

        out["StartCondition"] = aws_sdk_pinpoint.types.start_condition.serialize_json(
            value["start_condition"]
        )
    if "state" in value:
        import aws_sdk_pinpoint.types.state

        out["State"] = aws_sdk_pinpoint.types.state.serialize_json(value["state"])
    if "wait_for_quiet_time" in value:
        out["WaitForQuietTime"] = value["wait_for_quiet_time"]
    if "refresh_on_segment_update" in value:
        out["RefreshOnSegmentUpdate"] = value["refresh_on_segment_update"]
    if "journey_channel_settings" in value:
        import aws_sdk_pinpoint.types.journey_channel_settings

        out["JourneyChannelSettings"] = (
            aws_sdk_pinpoint.types.journey_channel_settings.serialize_json(
                value["journey_channel_settings"]
            )
        )
    if "sending_schedule" in value:
        out["SendingSchedule"] = value["sending_schedule"]
    if "open_hours" in value:
        import aws_sdk_pinpoint.types.open_hours

        out["OpenHours"] = aws_sdk_pinpoint.types.open_hours.serialize_json(
            value["open_hours"]
        )
    if "closed_days" in value:
        import aws_sdk_pinpoint.types.closed_days

        out["ClosedDays"] = aws_sdk_pinpoint.types.closed_days.serialize_json(
            value["closed_days"]
        )
    if "timezone_estimation_methods" in value:
        import aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element

        out["TimezoneEstimationMethods"] = (
            aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element.serialize_json(
                value["timezone_estimation_methods"]
            )
        )
    return out


def deserialize_json(data: dict) -> WriteJourneyRequest:
    out: WriteJourneyRequest = {}  # type: ignore[typeddict-item]
    if "Activities" in data:
        import aws_sdk_pinpoint.types.map_of_activity

        out["activities"] = aws_sdk_pinpoint.types.map_of_activity.deserialize_json(
            data["Activities"]
        )
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Limits" in data:
        import aws_sdk_pinpoint.types.journey_limits

        out["limits"] = aws_sdk_pinpoint.types.journey_limits.deserialize_json(
            data["Limits"]
        )
    if "LocalTime" in data:
        out["local_time"] = data["LocalTime"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "QuietTime" in data:
        import aws_sdk_pinpoint.types.quiet_time

        out["quiet_time"] = aws_sdk_pinpoint.types.quiet_time.deserialize_json(
            data["QuietTime"]
        )
    if "RefreshFrequency" in data:
        out["refresh_frequency"] = data["RefreshFrequency"]
    if "Schedule" in data:
        import aws_sdk_pinpoint.types.journey_schedule

        out["schedule"] = aws_sdk_pinpoint.types.journey_schedule.deserialize_json(
            data["Schedule"]
        )
    if "StartActivity" in data:
        out["start_activity"] = data["StartActivity"]
    if "StartCondition" in data:
        import aws_sdk_pinpoint.types.start_condition

        out["start_condition"] = (
            aws_sdk_pinpoint.types.start_condition.deserialize_json(
                data["StartCondition"]
            )
        )
    if "State" in data:
        import aws_sdk_pinpoint.types.state

        out["state"] = aws_sdk_pinpoint.types.state.deserialize_json(data["State"])
    if "WaitForQuietTime" in data:
        out["wait_for_quiet_time"] = data["WaitForQuietTime"]
    if "RefreshOnSegmentUpdate" in data:
        out["refresh_on_segment_update"] = data["RefreshOnSegmentUpdate"]
    if "JourneyChannelSettings" in data:
        import aws_sdk_pinpoint.types.journey_channel_settings

        out["journey_channel_settings"] = (
            aws_sdk_pinpoint.types.journey_channel_settings.deserialize_json(
                data["JourneyChannelSettings"]
            )
        )
    if "SendingSchedule" in data:
        out["sending_schedule"] = data["SendingSchedule"]
    if "OpenHours" in data:
        import aws_sdk_pinpoint.types.open_hours

        out["open_hours"] = aws_sdk_pinpoint.types.open_hours.deserialize_json(
            data["OpenHours"]
        )
    if "ClosedDays" in data:
        import aws_sdk_pinpoint.types.closed_days

        out["closed_days"] = aws_sdk_pinpoint.types.closed_days.deserialize_json(
            data["ClosedDays"]
        )
    if "TimezoneEstimationMethods" in data:
        import aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element

        out["timezone_estimation_methods"] = (
            aws_sdk_pinpoint.types.list_of__timezone_estimation_methods_element.deserialize_json(
                data["TimezoneEstimationMethods"]
            )
        )
    return out
