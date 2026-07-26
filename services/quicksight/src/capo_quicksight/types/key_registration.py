"""Generated from Smithy shape ``com.amazonaws.quicksight#KeyRegistration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.registered_customer_managed_key

KeyRegistration: TypeAlias = list[
    "capo_quicksight.types.registered_customer_managed_key.RegisteredCustomerManagedKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: KeyRegistration) -> list:
    import capo_quicksight.types.registered_customer_managed_key

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.registered_customer_managed_key.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KeyRegistration:
    import capo_quicksight.types.registered_customer_managed_key

    out: KeyRegistration = []
    for item in data:
        out.append(
            capo_quicksight.types.registered_customer_managed_key.deserialize_json(item)
        )
    return out
