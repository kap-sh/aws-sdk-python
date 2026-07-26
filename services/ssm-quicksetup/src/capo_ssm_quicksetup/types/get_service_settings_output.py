"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetServiceSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.service_settings


class GetServiceSettingsOutput(TypedDict, closed=True):
    service_settings: NotRequired[
        "capo_ssm_quicksetup.types.service_settings.ServiceSettings"
    ]
    """<p>Returns details about the settings for Quick Setup in the requesting Amazon Web Services account and Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceSettingsOutput) -> dict:
    out: dict = {}
    if "service_settings" in value:
        import capo_ssm_quicksetup.types.service_settings

        out["ServiceSettings"] = (
            capo_ssm_quicksetup.types.service_settings.serialize_json(
                value["service_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServiceSettingsOutput:
    out: GetServiceSettingsOutput = {}  # type: ignore[typeddict-item]
    if "ServiceSettings" in data:
        import capo_ssm_quicksetup.types.service_settings

        out["service_settings"] = (
            capo_ssm_quicksetup.types.service_settings.deserialize_json(
                data["ServiceSettings"]
            )
        )
    return out
