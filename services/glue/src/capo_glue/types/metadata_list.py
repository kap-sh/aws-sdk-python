"""Generated from Smithy shape ``com.amazonaws.glue#MetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.metadata_key_value_pair

MetadataList: TypeAlias = list[
    "capo_glue.types.metadata_key_value_pair.MetadataKeyValuePair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataList) -> list:
    import capo_glue.types.metadata_key_value_pair

    out: list = []
    for item in value:
        out.append(capo_glue.types.metadata_key_value_pair.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetadataList:
    import capo_glue.types.metadata_key_value_pair

    out: MetadataList = []
    for item in data:
        out.append(
            capo_glue.types.metadata_key_value_pair.deserialize_aws_json_1_1(item)
        )
    return out
