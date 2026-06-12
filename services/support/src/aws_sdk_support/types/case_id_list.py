"""Generated from Smithy shape ``com.amazonaws.support#CaseIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.case_id

CaseIdList: TypeAlias = list["aws_sdk_support.types.case_id.CaseId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CaseIdList:
    return list(data)
