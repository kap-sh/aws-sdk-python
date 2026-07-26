"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwarePackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.software_package

SoftwarePackageList: TypeAlias = list[
    "capo_securityhub.types.software_package.SoftwarePackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwarePackageList) -> list:
    import capo_securityhub.types.software_package

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.software_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> SoftwarePackageList:
    import capo_securityhub.types.software_package

    out: SoftwarePackageList = []
    for item in data:
        out.append(capo_securityhub.types.software_package.deserialize_json(item))
    return out
