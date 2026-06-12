"""Generated from Smithy shape ``com.amazonaws.glue#CatalogList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog

CatalogList: TypeAlias = list["aws_sdk_glue.types.catalog.Catalog"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogList) -> list:
    import aws_sdk_glue.types.catalog

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.catalog.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CatalogList:
    import aws_sdk_glue.types.catalog

    out: CatalogList = []
    for item in data:
        out.append(aws_sdk_glue.types.catalog.deserialize_aws_json_1_1(item))
    return out
