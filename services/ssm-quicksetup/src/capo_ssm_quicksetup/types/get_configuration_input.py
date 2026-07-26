"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationInput``."""

from typing_extensions import TypedDict


class GetConfigurationInput(TypedDict, closed=True):
    configuration_id: "str"
    """<p>A service generated identifier for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationInput:
    out: GetConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
