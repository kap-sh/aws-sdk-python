"""Generated from Smithy shape ``com.amazonaws.glue#EnableAdditionalMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.jdbc_metadata_entry

EnableAdditionalMetadata: TypeAlias = list[
    "capo_glue.types.jdbc_metadata_entry.JdbcMetadataEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableAdditionalMetadata) -> list:
    import capo_glue.types.jdbc_metadata_entry

    out: list = []
    for item in value:
        out.append(capo_glue.types.jdbc_metadata_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnableAdditionalMetadata:
    import capo_glue.types.jdbc_metadata_entry

    out: EnableAdditionalMetadata = []
    for item in data:
        out.append(capo_glue.types.jdbc_metadata_entry.deserialize_aws_json_1_1(item))
    return out
