"""Generated from Smithy shape ``com.amazonaws.eks#LicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.license

LicenseList: TypeAlias = list["aws_sdk_eks.types.license.License"]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseList) -> list:
    import aws_sdk_eks.types.license

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.license.serialize_json(item))
    return out


def deserialize_json(data: list) -> LicenseList:
    import aws_sdk_eks.types.license

    out: LicenseList = []
    for item in data:
        out.append(aws_sdk_eks.types.license.deserialize_json(item))
    return out
