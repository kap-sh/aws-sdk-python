"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration_parameter_name


class EnvironmentConfigurationParameter(TypedDict, closed=True):
    name: NotRequired[
        "capo_datazone.types.environment_configuration_parameter_name.EnvironmentConfigurationParameterName"
    ]
    """<p>The name of the environment configuration parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of the environment configuration parameter.</p>"""
    is_editable: NotRequired["bool"]
    """<p>Specifies whether the environment parameter is editable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "is_editable" in value:
        out["isEditable"] = value["is_editable"]
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationParameter:
    out: EnvironmentConfigurationParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    if "isEditable" in data:
        out["is_editable"] = data["isEditable"]
    return out
