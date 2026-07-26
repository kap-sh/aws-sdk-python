"""Generated from Smithy shape ``com.amazonaws.glue#DataSourceMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_source
    import capo_glue.types.name_string

DataSourceMap: TypeAlias = dict[
    "capo_glue.types.name_string.NameString", "capo_glue.types.data_source.DataSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DataSourceMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.data_source

        out[key] = capo_glue.types.data_source.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceMap:
    out: DataSourceMap = {}
    for key, value in data.items():
        import capo_glue.types.data_source

        out[key] = capo_glue.types.data_source.deserialize_aws_json_1_1(value)
    return out
