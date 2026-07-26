"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.connection_type_brief

ConnectionTypeList: TypeAlias = list[
    "capo_glue.types.connection_type_brief.ConnectionTypeBrief"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionTypeList) -> list:
    import capo_glue.types.connection_type_brief

    out: list = []
    for item in value:
        out.append(capo_glue.types.connection_type_brief.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionTypeList:
    import capo_glue.types.connection_type_brief

    out: ConnectionTypeList = []
    for item in data:
        out.append(capo_glue.types.connection_type_brief.deserialize_aws_json_1_1(item))
    return out
