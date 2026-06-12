"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Recommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.recommendation

Recommendations: TypeAlias = list[
    "aws_sdk_codeguruprofiler.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Recommendations) -> list:
    import aws_sdk_codeguruprofiler.types.recommendation

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguruprofiler.types.recommendation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Recommendations:
    import aws_sdk_codeguruprofiler.types.recommendation

    out: Recommendations = []
    for item in data:
        out.append(aws_sdk_codeguruprofiler.types.recommendation.deserialize_json(item))
    return out
