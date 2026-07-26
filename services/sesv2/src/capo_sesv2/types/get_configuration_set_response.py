"""Generated from Smithy shape ``com.amazonaws.sesv2#GetConfigurationSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.archiving_options
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.delivery_options
    import capo_sesv2.types.reputation_options
    import capo_sesv2.types.sending_options
    import capo_sesv2.types.suppression_options
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.tracking_options
    import capo_sesv2.types.vdm_options


class GetConfigurationSetResponse(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set.</p>"""
    tracking_options: NotRequired["capo_sesv2.types.tracking_options.TrackingOptions"]
    """<p>An object that defines the open and click tracking options for emails that you send using the configuration set.</p>"""
    delivery_options: NotRequired["capo_sesv2.types.delivery_options.DeliveryOptions"]
    """<p>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</p>"""
    reputation_options: NotRequired[
        "capo_sesv2.types.reputation_options.ReputationOptions"
    ]
    """<p>An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.</p>"""
    sending_options: NotRequired["capo_sesv2.types.sending_options.SendingOptions"]
    """<p>An object that defines whether or not Amazon SES can send email that you send using the configuration set.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that are associated with the configuration set.</p>"""
    suppression_options: NotRequired[
        "capo_sesv2.types.suppression_options.SuppressionOptions"
    ]
    """<p>An object that contains information about the suppression list preferences for your account or for a specific tenant.</p>"""
    vdm_options: NotRequired["capo_sesv2.types.vdm_options.VdmOptions"]
    """<p>An object that contains information about the VDM preferences for your configuration set.</p>"""
    archiving_options: NotRequired[
        "capo_sesv2.types.archiving_options.ArchivingOptions"
    ]
    """<p>An object that defines the MailManager archive where sent emails are archived that you send using the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationSetResponse) -> dict:
    out: dict = {}
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "tracking_options" in value:
        import capo_sesv2.types.tracking_options

        out["TrackingOptions"] = capo_sesv2.types.tracking_options.serialize_json(
            value["tracking_options"]
        )
    if "delivery_options" in value:
        import capo_sesv2.types.delivery_options

        out["DeliveryOptions"] = capo_sesv2.types.delivery_options.serialize_json(
            value["delivery_options"]
        )
    if "reputation_options" in value:
        import capo_sesv2.types.reputation_options

        out["ReputationOptions"] = capo_sesv2.types.reputation_options.serialize_json(
            value["reputation_options"]
        )
    if "sending_options" in value:
        import capo_sesv2.types.sending_options

        out["SendingOptions"] = capo_sesv2.types.sending_options.serialize_json(
            value["sending_options"]
        )
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "suppression_options" in value:
        import capo_sesv2.types.suppression_options

        out["SuppressionOptions"] = capo_sesv2.types.suppression_options.serialize_json(
            value["suppression_options"]
        )
    if "vdm_options" in value:
        import capo_sesv2.types.vdm_options

        out["VdmOptions"] = capo_sesv2.types.vdm_options.serialize_json(
            value["vdm_options"]
        )
    if "archiving_options" in value:
        import capo_sesv2.types.archiving_options

        out["ArchivingOptions"] = capo_sesv2.types.archiving_options.serialize_json(
            value["archiving_options"]
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationSetResponse:
    out: GetConfigurationSetResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if "TrackingOptions" in data:
        import capo_sesv2.types.tracking_options

        out["tracking_options"] = capo_sesv2.types.tracking_options.deserialize_json(
            data["TrackingOptions"]
        )
    if "DeliveryOptions" in data:
        import capo_sesv2.types.delivery_options

        out["delivery_options"] = capo_sesv2.types.delivery_options.deserialize_json(
            data["DeliveryOptions"]
        )
    if "ReputationOptions" in data:
        import capo_sesv2.types.reputation_options

        out["reputation_options"] = (
            capo_sesv2.types.reputation_options.deserialize_json(
                data["ReputationOptions"]
            )
        )
    if "SendingOptions" in data:
        import capo_sesv2.types.sending_options

        out["sending_options"] = capo_sesv2.types.sending_options.deserialize_json(
            data["SendingOptions"]
        )
    if "Tags" in data:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "SuppressionOptions" in data:
        import capo_sesv2.types.suppression_options

        out["suppression_options"] = (
            capo_sesv2.types.suppression_options.deserialize_json(
                data["SuppressionOptions"]
            )
        )
    if "VdmOptions" in data:
        import capo_sesv2.types.vdm_options

        out["vdm_options"] = capo_sesv2.types.vdm_options.deserialize_json(
            data["VdmOptions"]
        )
    if "ArchivingOptions" in data:
        import capo_sesv2.types.archiving_options

        out["archiving_options"] = capo_sesv2.types.archiving_options.deserialize_json(
            data["ArchivingOptions"]
        )
    return out
