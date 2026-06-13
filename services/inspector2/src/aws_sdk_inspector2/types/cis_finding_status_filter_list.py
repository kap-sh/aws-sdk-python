"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_finding_status_filter

CisFindingStatusFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_finding_status_filter.CisFindingStatusFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisFindingStatusFilterList) -> list:
    import aws_sdk_inspector2.types.cis_finding_status_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_finding_status_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CisFindingStatusFilterList:
    import aws_sdk_inspector2.types.cis_finding_status_filter

    out: CisFindingStatusFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_finding_status_filter.deserialize_json(item)
        )
    return out
