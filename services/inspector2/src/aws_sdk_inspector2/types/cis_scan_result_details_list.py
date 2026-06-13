"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_result_details

CisScanResultDetailsList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_scan_result_details.CisScanResultDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetailsList) -> list:
    import aws_sdk_inspector2.types.cis_scan_result_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_scan_result_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CisScanResultDetailsList:
    import aws_sdk_inspector2.types.cis_scan_result_details

    out: CisScanResultDetailsList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_scan_result_details.deserialize_json(item)
        )
    return out
