"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectContinuousIntegrationScanConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.project_continuous_integration_scan_configuration

ProjectContinuousIntegrationScanConfigurationList: TypeAlias = list[
    "capo_inspector2.types.project_continuous_integration_scan_configuration.ProjectContinuousIntegrationScanConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectContinuousIntegrationScanConfigurationList) -> list:
    import capo_inspector2.types.project_continuous_integration_scan_configuration

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.project_continuous_integration_scan_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProjectContinuousIntegrationScanConfigurationList:
    import capo_inspector2.types.project_continuous_integration_scan_configuration

    out: ProjectContinuousIntegrationScanConfigurationList = []
    for item in data:
        out.append(
            capo_inspector2.types.project_continuous_integration_scan_configuration.deserialize_json(
                item
            )
        )
    return out
