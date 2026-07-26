"""Generated from Smithy shape ``com.amazonaws.glue#CatalogEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.catalog_entry

CatalogEntries: TypeAlias = list["capo_glue.types.catalog_entry.CatalogEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogEntries) -> list:
    import capo_glue.types.catalog_entry

    out: list = []
    for item in value:
        out.append(capo_glue.types.catalog_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CatalogEntries:
    import capo_glue.types.catalog_entry

    out: CatalogEntries = []
    for item in data:
        out.append(capo_glue.types.catalog_entry.deserialize_aws_json_1_1(item))
    return out
