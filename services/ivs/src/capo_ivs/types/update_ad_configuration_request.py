"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateAdConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_arn
    import capo_ivs.types.ad_configuration_name
    import capo_ivs.types.media_tailor_playback_configurations_list


class UpdateAdConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn"
    """<p>ARN of the ad configuration to be updated.</p>"""
    name: NotRequired["capo_ivs.types.ad_configuration_name.AdConfigurationName"]
    """<p>Ad configuration name. The value does not need to be unique.</p>"""
    media_tailor_playback_configurations: NotRequired[
        "capo_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
    ]
    r"""<p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html\">Generate and Sign IVS Playback Tokens</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAdConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "media_tailor_playback_configurations" in value:
        import capo_ivs.types.media_tailor_playback_configurations_list

        out["mediaTailorPlaybackConfigurations"] = (
            capo_ivs.types.media_tailor_playback_configurations_list.serialize_json(
                value["media_tailor_playback_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAdConfigurationRequest:
    out: UpdateAdConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateAdConfigurationRequest.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "mediaTailorPlaybackConfigurations" in data:
        import capo_ivs.types.media_tailor_playback_configurations_list

        out["media_tailor_playback_configurations"] = (
            capo_ivs.types.media_tailor_playback_configurations_list.deserialize_json(
                data["mediaTailorPlaybackConfigurations"]
            )
        )
    return out
