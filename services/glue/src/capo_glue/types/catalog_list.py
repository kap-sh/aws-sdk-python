"""Generated from Smithy shape ``com.amazonaws.glue#CatalogList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.catalog

CatalogList: TypeAlias = list["capo_glue.types.catalog.Catalog"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogList) -> list:
    import capo_glue.types.catalog

    out: list = []
    for item in value:
        out.append(capo_glue.types.catalog.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CatalogList:
    import capo_glue.types.catalog

    out: CatalogList = []
    for item in data:
        out.append(capo_glue.types.catalog.deserialize_aws_json_1_1(item))
    return out
