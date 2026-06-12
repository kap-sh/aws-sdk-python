"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FilterCriteriaMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.criterion

FilterCriteriaMap: TypeAlias = dict[
    "str", "aws_sdk_accessanalyzer.types.criterion.Criterion"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FilterCriteriaMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_accessanalyzer.types.criterion

        out[key] = aws_sdk_accessanalyzer.types.criterion.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FilterCriteriaMap:
    out: FilterCriteriaMap = {}
    for key, value in data.items():
        import aws_sdk_accessanalyzer.types.criterion

        out[key] = aws_sdk_accessanalyzer.types.criterion.deserialize_json(value)
    return out
