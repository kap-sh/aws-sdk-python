"""Generated from Smithy shape ``com.amazonaws.odb#DbSystemShapeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.db_system_shape_summary

DbSystemShapeList: TypeAlias = list[
    "capo_odb.types.db_system_shape_summary.DbSystemShapeSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbSystemShapeList) -> list:
    import capo_odb.types.db_system_shape_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.db_system_shape_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DbSystemShapeList:
    import capo_odb.types.db_system_shape_summary

    out: DbSystemShapeList = []
    for item in data:
        out.append(
            capo_odb.types.db_system_shape_summary.deserialize_aws_json_1_0(item)
        )
    return out
