"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_parameters_map


class ConfigurationDefinitionSummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""
    type: NotRequired["str"]
    """<p>The type of the Quick Setup configuration used by the configuration definition.</p>"""
    type_version: NotRequired["str"]
    """<p>The version of the Quick Setup type used by the configuration definition.</p>"""
    first_class_parameters: NotRequired[
        "capo_ssm_quicksetup.types.configuration_parameters_map.ConfigurationParametersMap"
    ]
    """<p>The common parameters and values for the configuration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDefinitionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        out["Type"] = value["type"]
    if "type_version" in value:
        out["TypeVersion"] = value["type_version"]
    if "first_class_parameters" in value:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["FirstClassParameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.serialize_json(
                value["first_class_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationDefinitionSummary:
    out: ConfigurationDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "TypeVersion" in data:
        out["type_version"] = data["TypeVersion"]
    if "FirstClassParameters" in data:
        import capo_ssm_quicksetup.types.configuration_parameters_map

        out["first_class_parameters"] = (
            capo_ssm_quicksetup.types.configuration_parameters_map.deserialize_json(
                data["FirstClassParameters"]
            )
        )
    return out
