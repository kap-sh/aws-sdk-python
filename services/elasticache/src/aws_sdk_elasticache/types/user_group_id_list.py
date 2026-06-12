"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user_group_id

UserGroupIdList: TypeAlias = list["aws_sdk_elasticache.types.user_group_id.UserGroupId"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> UserGroupIdList:
    out: UserGroupIdList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: UserGroupIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> UserGroupIdList:
    out: UserGroupIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
