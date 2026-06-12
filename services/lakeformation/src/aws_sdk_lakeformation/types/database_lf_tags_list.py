"""Generated from Smithy shape ``com.amazonaws.lakeformation#DatabaseLFTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.tagged_database

DatabaseLFTagsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.tagged_database.TaggedDatabase"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseLFTagsList) -> list:
    import aws_sdk_lakeformation.types.tagged_database

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.tagged_database.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatabaseLFTagsList:
    import aws_sdk_lakeformation.types.tagged_database

    out: DatabaseLFTagsList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.tagged_database.deserialize_json(item))
    return out
