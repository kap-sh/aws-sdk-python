"""Generated from Smithy shape ``com.amazonaws.support#CaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.case_details

CaseList: TypeAlias = list["capo_support.types.case_details.CaseDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseList) -> list:
    import capo_support.types.case_details

    out: list = []
    for item in value:
        out.append(capo_support.types.case_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CaseList:
    import capo_support.types.case_details

    out: CaseList = []
    for item in data:
        out.append(capo_support.types.case_details.deserialize_aws_json_1_1(item))
    return out
