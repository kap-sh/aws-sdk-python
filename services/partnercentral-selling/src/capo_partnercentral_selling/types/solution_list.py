"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SolutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.solution_base

SolutionList: TypeAlias = list[
    "capo_partnercentral_selling.types.solution_base.SolutionBase"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SolutionList) -> list:
    import capo_partnercentral_selling.types.solution_base

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.solution_base.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SolutionList:
    import capo_partnercentral_selling.types.solution_base

    out: SolutionList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.solution_base.deserialize_aws_json_1_0(
                item
            )
        )
    return out
