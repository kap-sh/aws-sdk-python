"""Generated from Smithy shape ``com.amazonaws.rds#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_target

TargetList: TypeAlias = list["aws_sdk_rds.types.db_proxy_target.DBProxyTarget"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_proxy_target

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_proxy_target.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetList:
    import aws_sdk_rds.types.db_proxy_target

    out: TargetList = []
    for child in el.findall("member"):
        out.append(aws_sdk_rds.types.db_proxy_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TargetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_proxy_target

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_proxy_target.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TargetList:
    import aws_sdk_rds.types.db_proxy_target

    out: TargetList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_proxy_target.deserialize_query(child))
    return out
