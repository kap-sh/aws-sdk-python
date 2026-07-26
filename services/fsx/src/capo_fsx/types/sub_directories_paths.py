"""Generated from Smithy shape ``com.amazonaws.fsx#SubDirectoriesPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.namespace

SubDirectoriesPaths: TypeAlias = list["capo_fsx.types.namespace.Namespace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubDirectoriesPaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubDirectoriesPaths:
    return list(data)
