"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Recommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommendation

Recommendations: TypeAlias = list[
    "capo_customer_profiles.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Recommendations) -> list:
    import capo_customer_profiles.types.recommendation

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recommendations:
    import capo_customer_profiles.types.recommendation

    out: Recommendations = []
    for item in data:
        out.append(capo_customer_profiles.types.recommendation.deserialize_json(item))
    return out
