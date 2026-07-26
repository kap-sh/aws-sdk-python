"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedAccountWithIncompleteSetup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data
    import capo_socialmessaging.types.whats_app_business_account_id

LinkedAccountWithIncompleteSetup: TypeAlias = dict[
    "capo_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId",
    "capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data.LinkedWhatsAppBusinessAccountIdMetaData",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LinkedAccountWithIncompleteSetup) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data

        out[key] = (
            capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> LinkedAccountWithIncompleteSetup:
    out: LinkedAccountWithIncompleteSetup = {}
    for key, value in data.items():
        import capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data

        out[key] = (
            capo_socialmessaging.types.linked_whats_app_business_account_id_meta_data.deserialize_json(
                value
            )
        )
    return out
