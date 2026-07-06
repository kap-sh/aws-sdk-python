"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.archiving_options
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.delivery_options
    import aws_sdk_sesv2.types.reputation_options
    import aws_sdk_sesv2.types.sending_options
    import aws_sdk_sesv2.types.suppression_options
    import aws_sdk_sesv2.types.tag_list
    import aws_sdk_sesv2.types.tracking_options
    import aws_sdk_sesv2.types.vdm_options


class CreateConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (_) only.</p>"""
    tracking_options: NotRequired[
        "aws_sdk_sesv2.types.tracking_options.TrackingOptions"
    ]
    """<p>An object that defines the open and click tracking options for emails that you send using the configuration set.</p>"""
    delivery_options: NotRequired[
        "aws_sdk_sesv2.types.delivery_options.DeliveryOptions"
    ]
    """<p>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</p>"""
    reputation_options: NotRequired[
        "aws_sdk_sesv2.types.reputation_options.ReputationOptions"
    ]
    """<p>An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.</p>"""
    sending_options: NotRequired["aws_sdk_sesv2.types.sending_options.SendingOptions"]
    """<p>An object that defines whether or not Amazon SES can send email that you send using the configuration set.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the configuration set.</p>"""
    suppression_options: NotRequired[
        "aws_sdk_sesv2.types.suppression_options.SuppressionOptions"
    ]
    """<p>An object that contains information about the suppression list preferences for the configuration set. You can optionally include a <code>SuppressionScope</code> to override the tenant or account suppression scope for emails sent using this configuration set.</p>"""
    vdm_options: NotRequired["aws_sdk_sesv2.types.vdm_options.VdmOptions"]
    """<p>An object that defines the VDM options for emails that you send using the configuration set.</p>"""
    archiving_options: NotRequired[
        "aws_sdk_sesv2.types.archiving_options.ArchivingOptions"
    ]
    """<p>An object that defines the MailManager archiving options for emails that you send using the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    if "tracking_options" in value:
        import aws_sdk_sesv2.types.tracking_options

        out["TrackingOptions"] = aws_sdk_sesv2.types.tracking_options.serialize_json(
            value["tracking_options"]
        )
    if "delivery_options" in value:
        import aws_sdk_sesv2.types.delivery_options

        out["DeliveryOptions"] = aws_sdk_sesv2.types.delivery_options.serialize_json(
            value["delivery_options"]
        )
    if "reputation_options" in value:
        import aws_sdk_sesv2.types.reputation_options

        out["ReputationOptions"] = (
            aws_sdk_sesv2.types.reputation_options.serialize_json(
                value["reputation_options"]
            )
        )
    if "sending_options" in value:
        import aws_sdk_sesv2.types.sending_options

        out["SendingOptions"] = aws_sdk_sesv2.types.sending_options.serialize_json(
            value["sending_options"]
        )
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    if "suppression_options" in value:
        import aws_sdk_sesv2.types.suppression_options

        out["SuppressionOptions"] = (
            aws_sdk_sesv2.types.suppression_options.serialize_json(
                value["suppression_options"]
            )
        )
    if "vdm_options" in value:
        import aws_sdk_sesv2.types.vdm_options

        out["VdmOptions"] = aws_sdk_sesv2.types.vdm_options.serialize_json(
            value["vdm_options"]
        )
    if "archiving_options" in value:
        import aws_sdk_sesv2.types.archiving_options

        out["ArchivingOptions"] = aws_sdk_sesv2.types.archiving_options.serialize_json(
            value["archiving_options"]
        )
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetRequest:
    out: CreateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "CreateConfigurationSetRequest.configuration_set_name required"
        )
    if "TrackingOptions" in data:
        import aws_sdk_sesv2.types.tracking_options

        out["tracking_options"] = aws_sdk_sesv2.types.tracking_options.deserialize_json(
            data["TrackingOptions"]
        )
    if "DeliveryOptions" in data:
        import aws_sdk_sesv2.types.delivery_options

        out["delivery_options"] = aws_sdk_sesv2.types.delivery_options.deserialize_json(
            data["DeliveryOptions"]
        )
    if "ReputationOptions" in data:
        import aws_sdk_sesv2.types.reputation_options

        out["reputation_options"] = (
            aws_sdk_sesv2.types.reputation_options.deserialize_json(
                data["ReputationOptions"]
            )
        )
    if "SendingOptions" in data:
        import aws_sdk_sesv2.types.sending_options

        out["sending_options"] = aws_sdk_sesv2.types.sending_options.deserialize_json(
            data["SendingOptions"]
        )
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "SuppressionOptions" in data:
        import aws_sdk_sesv2.types.suppression_options

        out["suppression_options"] = (
            aws_sdk_sesv2.types.suppression_options.deserialize_json(
                data["SuppressionOptions"]
            )
        )
    if "VdmOptions" in data:
        import aws_sdk_sesv2.types.vdm_options

        out["vdm_options"] = aws_sdk_sesv2.types.vdm_options.deserialize_json(
            data["VdmOptions"]
        )
    if "ArchivingOptions" in data:
        import aws_sdk_sesv2.types.archiving_options

        out["archiving_options"] = (
            aws_sdk_sesv2.types.archiving_options.deserialize_json(
                data["ArchivingOptions"]
            )
        )
    return out
