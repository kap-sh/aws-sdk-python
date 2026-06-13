"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_result_status_filter

CisResultStatusFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_result_status_filter.CisResultStatusFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatusFilterList) -> list:
    import aws_sdk_inspector2.types.cis_result_status_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_result_status_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CisResultStatusFilterList:
    import aws_sdk_inspector2.types.cis_result_status_filter

    out: CisResultStatusFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_result_status_filter.deserialize_json(item)
        )
    return out
