"""Generated from Smithy shape ``com.amazonaws.glue#TableVersionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.table_version_error

TableVersionErrors: TypeAlias = list[
    "capo_glue.types.table_version_error.TableVersionError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableVersionErrors) -> list:
    import capo_glue.types.table_version_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.table_version_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableVersionErrors:
    import capo_glue.types.table_version_error

    out: TableVersionErrors = []
    for item in data:
        out.append(capo_glue.types.table_version_error.deserialize_aws_json_1_1(item))
    return out
