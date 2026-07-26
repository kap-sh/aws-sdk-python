"""Generated from Smithy shape ``com.amazonaws.appconfig#GetConfigurationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id


class GetConfigurationProfileRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.id.Id"
    """<p>The ID of the application that includes the configuration profile you want to get.</p>"""
    configuration_profile_id: "capo_appconfig.types.id.Id"
    """<p>The ID of the configuration profile that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationProfileRequest:
    out: GetConfigurationProfileRequest = {}  # type: ignore[typeddict-item]
    return out
