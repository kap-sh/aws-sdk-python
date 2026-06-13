"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configuration

CisScanConfigurationList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_scan_configuration.CisScanConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanConfigurationList) -> list:
    import aws_sdk_inspector2.types.cis_scan_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cis_scan_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisScanConfigurationList:
    import aws_sdk_inspector2.types.cis_scan_configuration

    out: CisScanConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_scan_configuration.deserialize_json(item)
        )
    return out
