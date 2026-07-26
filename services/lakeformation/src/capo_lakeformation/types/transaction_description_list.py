"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.transaction_description

TransactionDescriptionList: TypeAlias = list[
    "capo_lakeformation.types.transaction_description.TransactionDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransactionDescriptionList) -> list:
    import capo_lakeformation.types.transaction_description

    out: list = []
    for item in value:
        out.append(
            capo_lakeformation.types.transaction_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TransactionDescriptionList:
    import capo_lakeformation.types.transaction_description

    out: TransactionDescriptionList = []
    for item in data:
        out.append(
            capo_lakeformation.types.transaction_description.deserialize_json(item)
        )
    return out
