"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#UpdateConfigurationManagerInput``."""

from typing_extensions import NotRequired, TypedDict


class UpdateConfigurationManagerInput(TypedDict, closed=True):
    manager_arn: "str"
    """<p>The ARN of the configuration manager.</p>"""
    name: NotRequired["str"]
    """<p>A name for the configuration manager.</p>"""
    description: NotRequired["str"]
    """<p>A description of the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationManagerInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationManagerInput:
    out: UpdateConfigurationManagerInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
