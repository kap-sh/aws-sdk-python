"""Generated from Smithy shape ``com.amazonaws.elasticache#UserGroupIdListInput``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.user_group_id

UserGroupIdListInput: TypeAlias = list[
    "capo_elasticache.types.user_group_id.UserGroupId"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserGroupIdListInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> UserGroupIdListInput:
    out: UserGroupIdListInput = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: UserGroupIdListInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> UserGroupIdListInput:
    out: UserGroupIdListInput = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
