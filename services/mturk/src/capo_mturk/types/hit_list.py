"""Generated from Smithy shape ``com.amazonaws.mturk#HITList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.hit

HITList: TypeAlias = list["capo_mturk.types.hit.HIT"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITList) -> list:
    import capo_mturk.types.hit

    out: list = []
    for item in value:
        out.append(capo_mturk.types.hit.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HITList:
    import capo_mturk.types.hit

    out: HITList = []
    for item in data:
        out.append(capo_mturk.types.hit.deserialize_aws_json_1_1(item))
    return out
