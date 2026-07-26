"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.configuration_options
    import capo_securityhub.types.non_empty_string


class ParameterDefinition(TypedDict, closed=True):
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Description of a control parameter. </p>"""
    configuration_options: NotRequired[
        "capo_securityhub.types.configuration_options.ConfigurationOptions"
    ]
    """<p> The options for customizing a control parameter. Customization options vary based on the data type of the parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_options" in value:
        import capo_securityhub.types.configuration_options

        out["ConfigurationOptions"] = (
            capo_securityhub.types.configuration_options.serialize_json(
                value["configuration_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterDefinition:
    out: ParameterDefinition = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConfigurationOptions" in data:
        import capo_securityhub.types.configuration_options

        out["configuration_options"] = (
            capo_securityhub.types.configuration_options.deserialize_json(
                data["ConfigurationOptions"]
            )
        )
    return out
