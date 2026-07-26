"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedCounterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.summarized_counter

SummarizedCounterList: TypeAlias = list[
    "capo_shield.types.summarized_counter.SummarizedCounter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedCounterList) -> list:
    import capo_shield.types.summarized_counter

    out: list = []
    for item in value:
        out.append(capo_shield.types.summarized_counter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SummarizedCounterList:
    import capo_shield.types.summarized_counter

    out: SummarizedCounterList = []
    for item in data:
        out.append(capo_shield.types.summarized_counter.deserialize_aws_json_1_1(item))
    return out
