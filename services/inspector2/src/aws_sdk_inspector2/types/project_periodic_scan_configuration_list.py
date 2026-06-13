"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectPeriodicScanConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.project_periodic_scan_configuration

ProjectPeriodicScanConfigurationList: TypeAlias = list[
    "aws_sdk_inspector2.types.project_periodic_scan_configuration.ProjectPeriodicScanConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectPeriodicScanConfigurationList) -> list:
    import aws_sdk_inspector2.types.project_periodic_scan_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.project_periodic_scan_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProjectPeriodicScanConfigurationList:
    import aws_sdk_inspector2.types.project_periodic_scan_configuration

    out: ProjectPeriodicScanConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.project_periodic_scan_configuration.deserialize_json(
                item
            )
        )
    return out
