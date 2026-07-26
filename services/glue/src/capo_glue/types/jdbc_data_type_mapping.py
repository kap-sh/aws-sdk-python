"""Generated from Smithy shape ``com.amazonaws.glue#JDBCDataTypeMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glue_record_type
    import capo_glue.types.jdbc_data_type

JDBCDataTypeMapping: TypeAlias = dict[
    "capo_glue.types.jdbc_data_type.JDBCDataType",
    "capo_glue.types.glue_record_type.GlueRecordType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: JDBCDataTypeMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.glue_record_type
        import capo_glue.types.jdbc_data_type

        out[capo_glue.types.jdbc_data_type.serialize_aws_json_1_1(key)] = (
            capo_glue.types.glue_record_type.serialize_aws_json_1_1(value)
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JDBCDataTypeMapping:
    out: JDBCDataTypeMapping = {}
    for key, value in data.items():
        import capo_glue.types.glue_record_type
        import capo_glue.types.jdbc_data_type

        out[capo_glue.types.jdbc_data_type.deserialize_aws_json_1_1(key)] = (
            capo_glue.types.glue_record_type.deserialize_aws_json_1_1(value)
        )
    return out
