"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.category

CategoryList: TypeAlias = list["aws_sdk_marketplace_discovery.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryList) -> list:
    import aws_sdk_marketplace_discovery.types.category

    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoryList:
    import aws_sdk_marketplace_discovery.types.category

    out: CategoryList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.category.deserialize_json(item))
    return out
