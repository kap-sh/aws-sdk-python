"""Generated from Smithy shape ``com.amazonaws.inspector#ExclusionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.exclusion

ExclusionMap: TypeAlias = dict[
    "capo_inspector.types.arn.Arn", "capo_inspector.types.exclusion.Exclusion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExclusionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_inspector.types.exclusion

        out[key] = capo_inspector.types.exclusion.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionMap:
    out: ExclusionMap = {}
    for key, value in data.items():
        import capo_inspector.types.exclusion

        out[key] = capo_inspector.types.exclusion.deserialize_aws_json_1_1(value)
    return out
