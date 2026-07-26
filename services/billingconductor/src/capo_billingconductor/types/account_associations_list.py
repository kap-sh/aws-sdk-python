"""Generated from Smithy shape ``com.amazonaws.billingconductor#AccountAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.account_associations_list_element

AccountAssociationsList: TypeAlias = list[
    "capo_billingconductor.types.account_associations_list_element.AccountAssociationsListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountAssociationsList) -> list:
    import capo_billingconductor.types.account_associations_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.account_associations_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountAssociationsList:
    import capo_billingconductor.types.account_associations_list_element

    out: AccountAssociationsList = []
    for item in data:
        out.append(
            capo_billingconductor.types.account_associations_list_element.deserialize_json(
                item
            )
        )
    return out
