"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Periods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.period

Periods: TypeAlias = list["capo_customer_profiles.types.period.Period"]


# --- restJson1 ser/de ---
def serialize_json(value: Periods) -> list:
    import capo_customer_profiles.types.period

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.period.serialize_json(item))
    return out


def deserialize_json(data: list) -> Periods:
    import capo_customer_profiles.types.period

    out: Periods = []
    for item in data:
        out.append(capo_customer_profiles.types.period.deserialize_json(item))
    return out
