"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.campaign_hook
    import capo_pinpoint.types.campaign_limits
    import capo_pinpoint.types.campaign_state
    import capo_pinpoint.types.custom_delivery_configuration
    import capo_pinpoint.types.list_of_treatment_resource
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.message_configuration
    import capo_pinpoint.types.schedule
    import capo_pinpoint.types.template_configuration


class CampaignResponse(TypedDict, closed=True):
    additional_treatments: NotRequired[
        "capo_pinpoint.types.list_of_treatment_resource.ListOfTreatmentResource"
    ]
    """<p>An array of responses, one for each treatment that you defined for the campaign, in addition to the default treatment.</p>"""
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the campaign applies to.</p>"""
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the campaign.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the campaign was created.</p>"""
    custom_delivery_configuration: NotRequired[
        "capo_pinpoint.types.custom_delivery_configuration.CustomDeliveryConfiguration"
    ]
    """<p>The delivery configuration settings for sending the campaign through a custom channel.</p>"""
    default_state: NotRequired["capo_pinpoint.types.campaign_state.CampaignState"]
    """<p>The current status of the campaign's default treatment. This value exists only for campaigns that have more than one treatment.</p>"""
    description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the campaign.</p>"""
    holdout_percent: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.</p>"""
    hook: NotRequired["capo_pinpoint.types.campaign_hook.CampaignHook"]
    """<p>The settings for the AWS Lambda function to use as a code hook for the campaign. You can use this hook to customize the segment that's used by the campaign.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the campaign.</p>"""
    is_paused: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the campaign is paused. A paused campaign doesn't run unless you resume it by changing this value to false.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date, in ISO 8601 format, when the campaign was last modified.</p>"""
    limits: NotRequired["capo_pinpoint.types.campaign_limits.CampaignLimits"]
    """<p>The messaging limits for the campaign.</p>"""
    message_configuration: NotRequired[
        "capo_pinpoint.types.message_configuration.MessageConfiguration"
    ]
    """<p>The message configuration settings for the campaign.</p>"""
    name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the campaign.</p>"""
    schedule: NotRequired["capo_pinpoint.types.schedule.Schedule"]
    """<p>The schedule settings for the campaign.</p>"""
    segment_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the segment that's associated with the campaign.</p>"""
    segment_version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The version number of the segment that's associated with the campaign.</p>"""
    state: NotRequired["capo_pinpoint.types.campaign_state.CampaignState"]
    """<p>The current status of the campaign.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A string-to-string map of key-value pairs that identifies the tags that are associated with the campaign. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_configuration: NotRequired[
        "capo_pinpoint.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The message template that’s used for the campaign.</p>"""
    treatment_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom description of the default treatment for the campaign.</p>"""
    treatment_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The custom name of the default treatment for the campaign, if the campaign has multiple treatments. A <i>treatment</i> is a variation of a campaign that's used for A/B testing.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The version number of the campaign.</p>"""
    priority: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>Defines the priority of the campaign, used to decide the order of messages displayed to user if there are multiple messages scheduled to be displayed at the same moment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignResponse) -> dict:
    out: dict = {}
    if "additional_treatments" in value:
        import capo_pinpoint.types.list_of_treatment_resource

        out["AdditionalTreatments"] = (
            capo_pinpoint.types.list_of_treatment_resource.serialize_json(
                value["additional_treatments"]
            )
        )
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "custom_delivery_configuration" in value:
        import capo_pinpoint.types.custom_delivery_configuration

        out["CustomDeliveryConfiguration"] = (
            capo_pinpoint.types.custom_delivery_configuration.serialize_json(
                value["custom_delivery_configuration"]
            )
        )
    if "default_state" in value:
        import capo_pinpoint.types.campaign_state

        out["DefaultState"] = capo_pinpoint.types.campaign_state.serialize_json(
            value["default_state"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "holdout_percent" in value:
        out["HoldoutPercent"] = value["holdout_percent"]
    if "hook" in value:
        import capo_pinpoint.types.campaign_hook

        out["Hook"] = capo_pinpoint.types.campaign_hook.serialize_json(value["hook"])
    if "id" in value:
        out["Id"] = value["id"]
    if "is_paused" in value:
        out["IsPaused"] = value["is_paused"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "limits" in value:
        import capo_pinpoint.types.campaign_limits

        out["Limits"] = capo_pinpoint.types.campaign_limits.serialize_json(
            value["limits"]
        )
    if "message_configuration" in value:
        import capo_pinpoint.types.message_configuration

        out["MessageConfiguration"] = (
            capo_pinpoint.types.message_configuration.serialize_json(
                value["message_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "schedule" in value:
        import capo_pinpoint.types.schedule

        out["Schedule"] = capo_pinpoint.types.schedule.serialize_json(value["schedule"])
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    if "segment_version" in value:
        out["SegmentVersion"] = value["segment_version"]
    if "state" in value:
        import capo_pinpoint.types.campaign_state

        out["State"] = capo_pinpoint.types.campaign_state.serialize_json(value["state"])
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_configuration" in value:
        import capo_pinpoint.types.template_configuration

        out["TemplateConfiguration"] = (
            capo_pinpoint.types.template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "treatment_description" in value:
        out["TreatmentDescription"] = value["treatment_description"]
    if "treatment_name" in value:
        out["TreatmentName"] = value["treatment_name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> CampaignResponse:
    out: CampaignResponse = {}  # type: ignore[typeddict-item]
    if "AdditionalTreatments" in data:
        import capo_pinpoint.types.list_of_treatment_resource

        out["additional_treatments"] = (
            capo_pinpoint.types.list_of_treatment_resource.deserialize_json(
                data["AdditionalTreatments"]
            )
        )
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    if "CustomDeliveryConfiguration" in data:
        import capo_pinpoint.types.custom_delivery_configuration

        out["custom_delivery_configuration"] = (
            capo_pinpoint.types.custom_delivery_configuration.deserialize_json(
                data["CustomDeliveryConfiguration"]
            )
        )
    if "DefaultState" in data:
        import capo_pinpoint.types.campaign_state

        out["default_state"] = capo_pinpoint.types.campaign_state.deserialize_json(
            data["DefaultState"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "HoldoutPercent" in data:
        out["holdout_percent"] = data["HoldoutPercent"]
    if "Hook" in data:
        import capo_pinpoint.types.campaign_hook

        out["hook"] = capo_pinpoint.types.campaign_hook.deserialize_json(data["Hook"])
    if "Id" in data:
        out["id"] = data["Id"]
    if "IsPaused" in data:
        out["is_paused"] = data["IsPaused"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Limits" in data:
        import capo_pinpoint.types.campaign_limits

        out["limits"] = capo_pinpoint.types.campaign_limits.deserialize_json(
            data["Limits"]
        )
    if "MessageConfiguration" in data:
        import capo_pinpoint.types.message_configuration

        out["message_configuration"] = (
            capo_pinpoint.types.message_configuration.deserialize_json(
                data["MessageConfiguration"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Schedule" in data:
        import capo_pinpoint.types.schedule

        out["schedule"] = capo_pinpoint.types.schedule.deserialize_json(
            data["Schedule"]
        )
    if "SegmentId" in data:
        out["segment_id"] = data["SegmentId"]
    if "SegmentVersion" in data:
        out["segment_version"] = data["SegmentVersion"]
    if "State" in data:
        import capo_pinpoint.types.campaign_state

        out["state"] = capo_pinpoint.types.campaign_state.deserialize_json(
            data["State"]
        )
    if "tags" in data:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if "TemplateConfiguration" in data:
        import capo_pinpoint.types.template_configuration

        out["template_configuration"] = (
            capo_pinpoint.types.template_configuration.deserialize_json(
                data["TemplateConfiguration"]
            )
        )
    if "TreatmentDescription" in data:
        out["treatment_description"] = data["TreatmentDescription"]
    if "TreatmentName" in data:
        out["treatment_name"] = data["TreatmentName"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
