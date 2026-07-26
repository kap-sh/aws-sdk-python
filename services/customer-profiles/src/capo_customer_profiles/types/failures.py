"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Failures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_query_failures

Failures: TypeAlias = list[
    "capo_customer_profiles.types.profile_query_failures.ProfileQueryFailures"
]


# --- restJson1 ser/de ---
def serialize_json(value: Failures) -> list:
    import capo_customer_profiles.types.profile_query_failures

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.profile_query_failures.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Failures:
    import capo_customer_profiles.types.profile_query_failures

    out: Failures = []
    for item in data:
        out.append(
            capo_customer_profiles.types.profile_query_failures.deserialize_json(item)
        )
    return out
