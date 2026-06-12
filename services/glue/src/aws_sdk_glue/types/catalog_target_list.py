"""Generated from Smithy shape ``com.amazonaws.glue#CatalogTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_target

CatalogTargetList: TypeAlias = list["aws_sdk_glue.types.catalog_target.CatalogTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogTargetList) -> list:
    import aws_sdk_glue.types.catalog_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.catalog_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CatalogTargetList:
    import aws_sdk_glue.types.catalog_target

    out: CatalogTargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.catalog_target.deserialize_aws_json_1_1(item))
    return out
