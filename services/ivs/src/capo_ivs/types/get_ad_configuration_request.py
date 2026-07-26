"""Generated from Smithy shape ``com.amazonaws.ivs#GetAdConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_arn


class GetAdConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn"
    """<p>ARN of the ad configuration to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetAdConfigurationRequest:
    out: GetAdConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetAdConfigurationRequest.arn required")
    return out
