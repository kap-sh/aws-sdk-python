"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration

CisScanConfigurationList: TypeAlias = list[
    "capo_inspector2.types.cis_scan_configuration.CisScanConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanConfigurationList) -> list:
    import capo_inspector2.types.cis_scan_configuration

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_scan_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisScanConfigurationList:
    import capo_inspector2.types.cis_scan_configuration

    out: CisScanConfigurationList = []
    for item in data:
        out.append(capo_inspector2.types.cis_scan_configuration.deserialize_json(item))
    return out
