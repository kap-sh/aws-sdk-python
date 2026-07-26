"""Generated from Smithy shape ``com.amazonaws.customerprofiles#foundByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.found_by_key_value

foundByList: TypeAlias = list[
    "capo_customer_profiles.types.found_by_key_value.FoundByKeyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: foundByList) -> list:
    import capo_customer_profiles.types.found_by_key_value

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.found_by_key_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> foundByList:
    import capo_customer_profiles.types.found_by_key_value

    out: foundByList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.found_by_key_value.deserialize_json(item)
        )
    return out
