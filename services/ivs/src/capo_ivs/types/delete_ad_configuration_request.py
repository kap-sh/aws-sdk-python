"""Generated from Smithy shape ``com.amazonaws.ivs#DeleteAdConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_arn


class DeleteAdConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn"
    """<p>ARN of the ad configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAdConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteAdConfigurationRequest:
    out: DeleteAdConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteAdConfigurationRequest.arn required")
    return out
