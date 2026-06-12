"""Generated from Smithy shape ``com.amazonaws.rds#DBEngineVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_engine_version

DBEngineVersionList: TypeAlias = list[
    "aws_sdk_rds.types.db_engine_version.DBEngineVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBEngineVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_engine_version.serialize_query(
            item, pairs, f"{prefix}.DBEngineVersion.{n}"
        )


def deserialize_query(el: Element) -> DBEngineVersionList:
    import aws_sdk_rds.types.db_engine_version

    out: DBEngineVersionList = []
    for child in el.findall("DBEngineVersion"):
        out.append(aws_sdk_rds.types.db_engine_version.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBEngineVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_engine_version.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBEngineVersionList:
    import aws_sdk_rds.types.db_engine_version

    out: DBEngineVersionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_engine_version.deserialize_query(child))
    return out
