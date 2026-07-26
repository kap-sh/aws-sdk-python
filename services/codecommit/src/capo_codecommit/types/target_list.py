"""Generated from Smithy shape ``com.amazonaws.codecommit#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.target

TargetList: TypeAlias = list["capo_codecommit.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetList) -> list:
    import capo_codecommit.types.target

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetList:
    import capo_codecommit.types.target

    out: TargetList = []
    for item in data:
        out.append(capo_codecommit.types.target.deserialize_aws_json_1_1(item))
    return out
