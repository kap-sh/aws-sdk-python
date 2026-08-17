"""Generated from Smithy shape ``com.amazonaws.ssm#MetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.metadata_key
    import capo_ssm.types.metadata_value

MetadataMap: TypeAlias = dict[
    "capo_ssm.types.metadata_key.MetadataKey",
    "capo_ssm.types.metadata_value.MetadataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.metadata_value

        out[key] = capo_ssm.types.metadata_value.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataMap:
    out: MetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_ssm.types.metadata_value

        out[key] = capo_ssm.types.metadata_value.deserialize_aws_json_1_1(value)
    return out
