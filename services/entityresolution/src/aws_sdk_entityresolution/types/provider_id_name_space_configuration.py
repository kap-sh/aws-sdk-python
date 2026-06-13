"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderIdNameSpaceConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ProviderIdNameSpaceConfiguration(TypedDict):
    description: NotRequired["str"]
    """<p>The description of the ID namespace.</p>"""
    provider_target_configuration_definition: NotRequired["object"]
    """<p>Configurations required for the target ID namespace.</p>"""
    provider_source_configuration_definition: NotRequired["object"]
    """<p>Configurations required for the source ID namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderIdNameSpaceConfiguration) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "provider_target_configuration_definition" in value:
        out["providerTargetConfigurationDefinition"] = value[
            "provider_target_configuration_definition"
        ]
    if "provider_source_configuration_definition" in value:
        out["providerSourceConfigurationDefinition"] = value[
            "provider_source_configuration_definition"
        ]
    return out


def deserialize_json(data: dict) -> ProviderIdNameSpaceConfiguration:
    out: ProviderIdNameSpaceConfiguration = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "providerTargetConfigurationDefinition" in data:
        out["provider_target_configuration_definition"] = data[
            "providerTargetConfigurationDefinition"
        ]
    if "providerSourceConfigurationDefinition" in data:
        out["provider_source_configuration_definition"] = data[
            "providerSourceConfigurationDefinition"
        ]
    return out
