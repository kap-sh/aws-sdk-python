"""Generated from Smithy shape ``com.amazonaws.glue#GetTableVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.table_version

GetTableVersionsList: TypeAlias = list["capo_glue.types.table_version.TableVersion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableVersionsList) -> list:
    import capo_glue.types.table_version

    out: list = []
    for item in value:
        out.append(capo_glue.types.table_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GetTableVersionsList:
    import capo_glue.types.table_version

    out: GetTableVersionsList = []
    for item in data:
        out.append(capo_glue.types.table_version.deserialize_aws_json_1_1(item))
    return out
