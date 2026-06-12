"""Generated from Smithy shape ``com.amazonaws.ssm#MetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.metadata_key
    import aws_sdk_ssm.types.metadata_value

MetadataMap: TypeAlias = dict[
    "aws_sdk_ssm.types.metadata_key.MetadataKey",
    "aws_sdk_ssm.types.metadata_value.MetadataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.metadata_value

        out[key] = aws_sdk_ssm.types.metadata_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataMap:
    out: MetadataMap = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.metadata_value

        out[key] = aws_sdk_ssm.types.metadata_value.deserialize_aws_json_1_1(value)
    return out
