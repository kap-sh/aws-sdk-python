"""Generated from Smithy shape ``com.amazonaws.pinpoint#ApplicationSettingsResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.application_settings_journey_limits
    import capo_pinpoint.types.campaign_hook
    import capo_pinpoint.types.campaign_limits
    import capo_pinpoint.types.quiet_time


class ApplicationSettingsResource(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    campaign_hook: NotRequired["capo_pinpoint.types.campaign_hook.CampaignHook"]
    """<p>The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the application's settings were last modified.</p>"""
    limits: NotRequired["capo_pinpoint.types.campaign_limits.CampaignLimits"]
    """<p>The default sending limits for campaigns in the application.</p>"""
    quiet_time: NotRequired["capo_pinpoint.types.quiet_time.QuietTime"]
    """<p>The default quiet time for campaigns in the application. Quiet time is a specific time range when messages aren't sent to endpoints, if all the following conditions are met:</p> <ul><li><p>The EndpointDemographic.Timezone property of the endpoint is set to a valid value.</p></li> <li><p>The current time in the endpoint's time zone is later than or equal to the time specified by the QuietTime.Start property for the application (or a campaign or journey that has custom quiet time settings).</p></li> <li><p>The current time in the endpoint's time zone is earlier than or equal to the time specified by the QuietTime.End property for the application (or a campaign or journey that has custom quiet time settings).</p></li></ul> <p>If any of the preceding conditions isn't met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled.</p>"""
    journey_limits: NotRequired[
        "capo_pinpoint.types.application_settings_journey_limits.ApplicationSettingsJourneyLimits"
    ]
    """<p>The default sending limits for journeys in the application. These limits apply to each journey for the application but can be overridden, on a per journey basis, with the JourneyLimits resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSettingsResource) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "campaign_hook" in value:
        import capo_pinpoint.types.campaign_hook

        out["CampaignHook"] = capo_pinpoint.types.campaign_hook.serialize_json(
            value["campaign_hook"]
        )
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "limits" in value:
        import capo_pinpoint.types.campaign_limits

        out["Limits"] = capo_pinpoint.types.campaign_limits.serialize_json(
            value["limits"]
        )
    if "quiet_time" in value:
        import capo_pinpoint.types.quiet_time

        out["QuietTime"] = capo_pinpoint.types.quiet_time.serialize_json(
            value["quiet_time"]
        )
    if "journey_limits" in value:
        import capo_pinpoint.types.application_settings_journey_limits

        out["JourneyLimits"] = (
            capo_pinpoint.types.application_settings_journey_limits.serialize_json(
                value["journey_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationSettingsResource:
    out: ApplicationSettingsResource = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "CampaignHook" in data:
        import capo_pinpoint.types.campaign_hook

        out["campaign_hook"] = capo_pinpoint.types.campaign_hook.deserialize_json(
            data["CampaignHook"]
        )
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Limits" in data:
        import capo_pinpoint.types.campaign_limits

        out["limits"] = capo_pinpoint.types.campaign_limits.deserialize_json(
            data["Limits"]
        )
    if "QuietTime" in data:
        import capo_pinpoint.types.quiet_time

        out["quiet_time"] = capo_pinpoint.types.quiet_time.deserialize_json(
            data["QuietTime"]
        )
    if "JourneyLimits" in data:
        import capo_pinpoint.types.application_settings_journey_limits

        out["journey_limits"] = (
            capo_pinpoint.types.application_settings_journey_limits.deserialize_json(
                data["JourneyLimits"]
            )
        )
    return out
