"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceContributorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.space_contributor

SpaceContributorList: TypeAlias = list[
    "aws_sdk_quicksight.types.space_contributor.SpaceContributor"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceContributorList) -> list:
    import aws_sdk_quicksight.types.space_contributor

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.space_contributor.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpaceContributorList:
    import aws_sdk_quicksight.types.space_contributor

    out: SpaceContributorList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.space_contributor.deserialize_json(item))
    return out
