"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateAdConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration


class UpdateAdConfigurationResponse(TypedDict, closed=True):
    ad_configuration: "capo_ivs.types.ad_configuration.AdConfiguration"
    """<p>Object specifying the updated ad configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAdConfigurationResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.ad_configuration

    out["adConfiguration"] = capo_ivs.types.ad_configuration.serialize_json(
        value["ad_configuration"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAdConfigurationResponse:
    out: UpdateAdConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "adConfiguration" in data:
        import capo_ivs.types.ad_configuration

        out["ad_configuration"] = capo_ivs.types.ad_configuration.deserialize_json(
            data["adConfiguration"]
        )
    else:
        raise DeserializationError(
            "UpdateAdConfigurationResponse.ad_configuration required"
        )
    return out
