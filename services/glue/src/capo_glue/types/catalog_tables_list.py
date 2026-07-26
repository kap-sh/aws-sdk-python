"""Generated from Smithy shape ``com.amazonaws.glue#CatalogTablesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.name_string

CatalogTablesList: TypeAlias = list["capo_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogTablesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CatalogTablesList:
    return list(data)
