"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#DeleteConfigurationManagerInput``."""

from typing import TypedDict


class DeleteConfigurationManagerInput(TypedDict):
    manager_arn: "str"
    """<p>The ID of the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationManagerInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfigurationManagerInput:
    out: DeleteConfigurationManagerInput = {}  # type: ignore[typeddict-item]
    return out
