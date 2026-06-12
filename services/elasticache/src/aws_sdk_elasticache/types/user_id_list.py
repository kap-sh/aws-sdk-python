"""Generated from Smithy shape ``com.amazonaws.elasticache#UserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.user_id

UserIdList: TypeAlias = list["aws_sdk_elasticache.types.user_id.UserId"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> UserIdList:
    out: UserIdList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: UserIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> UserIdList:
    out: UserIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
