"""Generated from Smithy shape ``com.amazonaws.ivs#AdConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration_arn
    import aws_sdk_ivs.types.ad_configuration_name
    import aws_sdk_ivs.types.media_tailor_playback_configurations_list
    import aws_sdk_ivs.types.tags


class AdConfigurationSummary(TypedDict, closed=True):
    arn: "aws_sdk_ivs.types.ad_configuration_arn.AdConfigurationArn"
    """<p>Ad configuration ARN.</p>"""
    name: NotRequired["aws_sdk_ivs.types.ad_configuration_name.AdConfigurationName"]
    """<p>Ad configuration name. Defaults to “”.</p>"""
    media_tailor_playback_configurations: "aws_sdk_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
    r"""<p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html\">Generate and Sign IVS Playback Tokens</a>.</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdConfigurationSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
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


def deserialize_json(data: dict) -> AdConfigurationSummary:
    out: AdConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AdConfigurationSummary.arn required")
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
            "AdConfigurationSummary.media_tailor_playback_configurations required"
        )
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    return out
