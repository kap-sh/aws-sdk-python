"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Recommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommendation

Recommendations: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Recommendations) -> list:
    import aws_sdk_customer_profiles.types.recommendation

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recommendations:
    import aws_sdk_customer_profiles.types.recommendation

    out: Recommendations = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommendation.deserialize_json(item)
        )
    return out
