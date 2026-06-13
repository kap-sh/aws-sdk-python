"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UseCaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.use_case_entry

UseCaseList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.use_case_entry.UseCaseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseList) -> list:
    import aws_sdk_marketplace_discovery.types.use_case_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.use_case_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UseCaseList:
    import aws_sdk_marketplace_discovery.types.use_case_entry

    out: UseCaseList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.use_case_entry.deserialize_json(item)
        )
    return out
