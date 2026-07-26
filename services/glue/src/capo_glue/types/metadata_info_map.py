"""Generated from Smithy shape ``com.amazonaws.glue#MetadataInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.metadata_info
    import capo_glue.types.metadata_key_string

MetadataInfoMap: TypeAlias = dict[
    "capo_glue.types.metadata_key_string.MetadataKeyString",
    "capo_glue.types.metadata_info.MetadataInfo",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MetadataInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.metadata_info

        out[key] = capo_glue.types.metadata_info.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataInfoMap:
    out: MetadataInfoMap = {}
    for key, value in data.items():
        import capo_glue.types.metadata_info

        out[key] = capo_glue.types.metadata_info.deserialize_aws_json_1_1(value)
    return out
