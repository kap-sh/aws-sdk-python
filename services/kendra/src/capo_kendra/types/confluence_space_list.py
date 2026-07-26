"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceSpaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.confluence_space_identifier

ConfluenceSpaceList: TypeAlias = list[
    "capo_kendra.types.confluence_space_identifier.ConfluenceSpaceIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceSpaceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfluenceSpaceList:
    return list(data)
