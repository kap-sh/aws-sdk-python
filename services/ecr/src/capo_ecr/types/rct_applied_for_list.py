"""Generated from Smithy shape ``com.amazonaws.ecr#RCTAppliedForList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.rct_applied_for

RCTAppliedForList: TypeAlias = list["capo_ecr.types.rct_applied_for.RCTAppliedFor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RCTAppliedForList) -> list:
    import capo_ecr.types.rct_applied_for

    out: list = []
    for item in value:
        out.append(capo_ecr.types.rct_applied_for.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RCTAppliedForList:
    import capo_ecr.types.rct_applied_for

    out: RCTAppliedForList = []
    for item in data:
        out.append(capo_ecr.types.rct_applied_for.deserialize_aws_json_1_1(item))
    return out
