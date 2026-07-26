"""Generated from Smithy shape ``com.amazonaws.glue#ErrorByName``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.error_detail
    import capo_glue.types.name_string

ErrorByName: TypeAlias = dict[
    "capo_glue.types.name_string.NameString", "capo_glue.types.error_detail.ErrorDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ErrorByName) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.error_detail

        out[key] = capo_glue.types.error_detail.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorByName:
    out: ErrorByName = {}
    for key, value in data.items():
        import capo_glue.types.error_detail

        out[key] = capo_glue.types.error_detail.deserialize_aws_json_1_1(value)
    return out
