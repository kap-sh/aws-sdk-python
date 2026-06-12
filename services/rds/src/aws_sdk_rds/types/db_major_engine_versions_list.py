"""Generated from Smithy shape ``com.amazonaws.rds#DBMajorEngineVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_major_engine_version

DBMajorEngineVersionsList: TypeAlias = list[
    "aws_sdk_rds.types.db_major_engine_version.DBMajorEngineVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBMajorEngineVersionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_major_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_major_engine_version.serialize_query(
            item, pairs, f"{prefix}.DBMajorEngineVersion.{n}"
        )


def deserialize_query(el: Element) -> DBMajorEngineVersionsList:
    import aws_sdk_rds.types.db_major_engine_version

    out: DBMajorEngineVersionsList = []
    for child in el.findall("DBMajorEngineVersion"):
        out.append(aws_sdk_rds.types.db_major_engine_version.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBMajorEngineVersionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_major_engine_version

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_major_engine_version.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBMajorEngineVersionsList:
    import aws_sdk_rds.types.db_major_engine_version

    out: DBMajorEngineVersionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_major_engine_version.deserialize_query(child))
    return out
