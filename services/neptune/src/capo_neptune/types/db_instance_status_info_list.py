"""Generated from Smithy shape ``com.amazonaws.neptune#DBInstanceStatusInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_instance_status_info

DBInstanceStatusInfoList: TypeAlias = list[
    "capo_neptune.types.db_instance_status_info.DBInstanceStatusInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceStatusInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.db_instance_status_info

    for n, item in enumerate(value, 1):
        capo_neptune.types.db_instance_status_info.serialize_query(
            item, pairs, f"{prefix}.DBInstanceStatusInfo.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceStatusInfoList:
    import capo_neptune.types.db_instance_status_info

    out: DBInstanceStatusInfoList = []
    for child in el.findall("DBInstanceStatusInfo"):
        out.append(capo_neptune.types.db_instance_status_info.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBInstanceStatusInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.db_instance_status_info

    for n, item in enumerate(value, 1):
        capo_neptune.types.db_instance_status_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBInstanceStatusInfoList:
    import capo_neptune.types.db_instance_status_info

    out: DBInstanceStatusInfoList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.db_instance_status_info.deserialize_query(child))
    return out
