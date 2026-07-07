"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectCodeSecurityScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list
    import aws_sdk_inspector2.types.project_periodic_scan_configuration_list


class ProjectCodeSecurityScanConfiguration(TypedDict, closed=True):
    periodic_scan_configurations: NotRequired[
        "aws_sdk_inspector2.types.project_periodic_scan_configuration_list.ProjectPeriodicScanConfigurationList"
    ]
    """<p>The periodic scan configurations applied to the project.</p>"""
    continuous_integration_scan_configurations: NotRequired[
        "aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list.ProjectContinuousIntegrationScanConfigurationList"
    ]
    """<p>The continuous integration scan configurations applied to the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectCodeSecurityScanConfiguration) -> dict:
    out: dict = {}
    if "periodic_scan_configurations" in value:
        import aws_sdk_inspector2.types.project_periodic_scan_configuration_list

        out["periodicScanConfigurations"] = (
            aws_sdk_inspector2.types.project_periodic_scan_configuration_list.serialize_json(
                value["periodic_scan_configurations"]
            )
        )
    if "continuous_integration_scan_configurations" in value:
        import aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list

        out["continuousIntegrationScanConfigurations"] = (
            aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list.serialize_json(
                value["continuous_integration_scan_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProjectCodeSecurityScanConfiguration:
    out: ProjectCodeSecurityScanConfiguration = {}  # type: ignore[typeddict-item]
    if "periodicScanConfigurations" in data:
        import aws_sdk_inspector2.types.project_periodic_scan_configuration_list

        out["periodic_scan_configurations"] = (
            aws_sdk_inspector2.types.project_periodic_scan_configuration_list.deserialize_json(
                data["periodicScanConfigurations"]
            )
        )
    if "continuousIntegrationScanConfigurations" in data:
        import aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list

        out["continuous_integration_scan_configurations"] = (
            aws_sdk_inspector2.types.project_continuous_integration_scan_configuration_list.deserialize_json(
                data["continuousIntegrationScanConfigurations"]
            )
        )
    return out
