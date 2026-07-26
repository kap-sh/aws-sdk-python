"""Generated from Smithy shape ``com.amazonaws.appconfig#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id


class GetEnvironmentRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.id.Id"
    """<p>The ID of the application that includes the environment you want to get.</p>"""
    environment_id: "capo_appconfig.types.id.Id"
    """<p>The ID of the environment that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
