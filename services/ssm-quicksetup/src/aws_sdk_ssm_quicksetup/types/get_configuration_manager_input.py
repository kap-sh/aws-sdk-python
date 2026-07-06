"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationManagerInput``."""

from typing_extensions import TypedDict


class GetConfigurationManagerInput(TypedDict, closed=True):
    manager_arn: "str"
    """<p>The ARN of the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationManagerInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfigurationManagerInput:
    out: GetConfigurationManagerInput = {}  # type: ignore[typeddict-item]
    return out
