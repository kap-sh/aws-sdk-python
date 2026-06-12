"""Generated from Smithy shape ``com.amazonaws.codeartifact#LicenseInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.license_info

LicenseInfoList: TypeAlias = list["aws_sdk_codeartifact.types.license_info.LicenseInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseInfoList) -> list:
    import aws_sdk_codeartifact.types.license_info

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.license_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> LicenseInfoList:
    import aws_sdk_codeartifact.types.license_info

    out: LicenseInfoList = []
    for item in data:
        out.append(aws_sdk_codeartifact.types.license_info.deserialize_json(item))
    return out
