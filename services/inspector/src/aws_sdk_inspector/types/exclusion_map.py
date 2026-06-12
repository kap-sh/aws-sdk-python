"""Generated from Smithy shape ``com.amazonaws.inspector#ExclusionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.exclusion

ExclusionMap: TypeAlias = dict[
    "aws_sdk_inspector.types.arn.Arn", "aws_sdk_inspector.types.exclusion.Exclusion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExclusionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_inspector.types.exclusion

        out[key] = aws_sdk_inspector.types.exclusion.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionMap:
    out: ExclusionMap = {}
    for key, value in data.items():
        import aws_sdk_inspector.types.exclusion

        out[key] = aws_sdk_inspector.types.exclusion.deserialize_aws_json_1_1(value)
    return out
