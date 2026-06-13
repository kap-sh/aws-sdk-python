"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan

CisScanList: TypeAlias = list["aws_sdk_inspector2.types.cis_scan.CisScan"]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanList) -> list:
    import aws_sdk_inspector2.types.cis_scan

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cis_scan.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisScanList:
    import aws_sdk_inspector2.types.cis_scan

    out: CisScanList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cis_scan.deserialize_json(item))
    return out
