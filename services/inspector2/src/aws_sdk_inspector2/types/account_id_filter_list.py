"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_string_filter

AccountIdFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_string_filter.CisStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdFilterList) -> list:
    import aws_sdk_inspector2.types.cis_string_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cis_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountIdFilterList:
    import aws_sdk_inspector2.types.cis_string_filter

    out: AccountIdFilterList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cis_string_filter.deserialize_json(item))
    return out
