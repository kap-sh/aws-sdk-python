"""Generated from Smithy shape ``com.amazonaws.glue#SortCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.sort_criterion

SortCriteria: TypeAlias = list["capo_glue.types.sort_criterion.SortCriterion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortCriteria) -> list:
    import capo_glue.types.sort_criterion

    out: list = []
    for item in value:
        out.append(capo_glue.types.sort_criterion.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SortCriteria:
    import capo_glue.types.sort_criterion

    out: SortCriteria = []
    for item in data:
        out.append(capo_glue.types.sort_criterion.deserialize_aws_json_1_1(item))
    return out
