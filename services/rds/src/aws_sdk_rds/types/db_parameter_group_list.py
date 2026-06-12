"""Generated from Smithy shape ``com.amazonaws.rds#DBParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_parameter_group

DBParameterGroupList: TypeAlias = list[
    "aws_sdk_rds.types.db_parameter_group.DBParameterGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_parameter_group

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_parameter_group.serialize_query(
            item, pairs, f"{prefix}.DBParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> DBParameterGroupList:
    import aws_sdk_rds.types.db_parameter_group

    out: DBParameterGroupList = []
    for child in el.findall("DBParameterGroup"):
        out.append(aws_sdk_rds.types.db_parameter_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_parameter_group

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_parameter_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBParameterGroupList:
    import aws_sdk_rds.types.db_parameter_group

    out: DBParameterGroupList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_parameter_group.deserialize_query(child))
    return out
