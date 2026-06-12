"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_filter

CaseFilterList: TypeAlias = list["aws_sdk_connectcases.types.case_filter.CaseFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseFilterList) -> list:
    import aws_sdk_connectcases.types.case_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.case_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseFilterList:
    import aws_sdk_connectcases.types.case_filter

    out: CaseFilterList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.case_filter.deserialize_json(item))
    return out
