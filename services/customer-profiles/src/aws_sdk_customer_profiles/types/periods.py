"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Periods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.period

Periods: TypeAlias = list["aws_sdk_customer_profiles.types.period.Period"]


# --- restJson1 ser/de ---
def serialize_json(value: Periods) -> list:
    import aws_sdk_customer_profiles.types.period

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.period.serialize_json(item))
    return out


def deserialize_json(data: list) -> Periods:
    import aws_sdk_customer_profiles.types.period

    out: Periods = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.period.deserialize_json(item))
    return out
