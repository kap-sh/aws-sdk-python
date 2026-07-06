"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.input_switch_configuration
    import aws_sdk_mediapackagev2.types.output_header_configuration
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name


class UpdateChannelRequest(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the channel for future identification purposes.</p>"""
    input_switch_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
    ]
    """<p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    output_header_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
    ]
    """<p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "input_switch_configuration" in value:
        import aws_sdk_mediapackagev2.types.input_switch_configuration

        out["InputSwitchConfiguration"] = (
            aws_sdk_mediapackagev2.types.input_switch_configuration.serialize_json(
                value["input_switch_configuration"]
            )
        )
    if "output_header_configuration" in value:
        import aws_sdk_mediapackagev2.types.output_header_configuration

        out["OutputHeaderConfiguration"] = (
            aws_sdk_mediapackagev2.types.output_header_configuration.serialize_json(
                value["output_header_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "InputSwitchConfiguration" in data:
        import aws_sdk_mediapackagev2.types.input_switch_configuration

        out["input_switch_configuration"] = (
            aws_sdk_mediapackagev2.types.input_switch_configuration.deserialize_json(
                data["InputSwitchConfiguration"]
            )
        )
    if "OutputHeaderConfiguration" in data:
        import aws_sdk_mediapackagev2.types.output_header_configuration

        out["output_header_configuration"] = (
            aws_sdk_mediapackagev2.types.output_header_configuration.deserialize_json(
                data["OutputHeaderConfiguration"]
            )
        )
    return out
