"""Generated from Smithy shape ``com.amazonaws.elasticache#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.user

UserList: TypeAlias = list["capo_elasticache.types.user.User"]


# --- awsQuery ser/de ---
def serialize_query(value: UserList, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elasticache.types.user

    for n, item in enumerate(value, 1):
        capo_elasticache.types.user.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> UserList:
    import capo_elasticache.types.user

    out: UserList = []
    for child in el.findall("member"):
        out.append(capo_elasticache.types.user.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UserList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.user

    for n, item in enumerate(value, 1):
        capo_elasticache.types.user.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> UserList:
    import capo_elasticache.types.user

    out: UserList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.user.deserialize_query(child))
    return out
