"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ErrorDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.error_detail

ErrorDetailList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.error_detail.ErrorDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetailList) -> list:
    import aws_sdk_marketplace_catalog.types.error_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_catalog.types.error_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorDetailList:
    import aws_sdk_marketplace_catalog.types.error_detail

    out: ErrorDetailList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.error_detail.deserialize_json(item)
        )
    return out
