"""Generated from Smithy shape ``com.amazonaws.ivs#CreateAdConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration_name
    import aws_sdk_ivs.types.media_tailor_playback_configurations_list
    import aws_sdk_ivs.types.tags


class CreateAdConfigurationRequest(TypedDict):
    name: NotRequired["aws_sdk_ivs.types.ad_configuration_name.AdConfigurationName"]
    """<p>Ad configuration name. Defaults to “”.</p>"""
    media_tailor_playback_configurations: "aws_sdk_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
    """<p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html\">Generate and Sign IVS Playback Tokens</a>.</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    """<p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAdConfigurationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import aws_sdk_ivs.types.media_tailor_playback_configurations_list

    out["mediaTailorPlaybackConfigurations"] = (
        aws_sdk_ivs.types.media_tailor_playback_configurations_list.serialize_json(
            value["media_tailor_playback_configurations"]
        )
    )
    if "tags" in value:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAdConfigurationRequest:
    out: CreateAdConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "mediaTailorPlaybackConfigurations" in data:
        import aws_sdk_ivs.types.media_tailor_playback_configurations_list

        out["media_tailor_playback_configurations"] = (
            aws_sdk_ivs.types.media_tailor_playback_configurations_list.deserialize_json(
                data["mediaTailorPlaybackConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAdConfigurationRequest.media_tailor_playback_configurations required"
        )
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    return out
