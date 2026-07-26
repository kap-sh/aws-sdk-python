"""Generated from Smithy shape ``com.amazonaws.elasticache#UserIdListInput``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.user_id

UserIdListInput: TypeAlias = list["capo_elasticache.types.user_id.UserId"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UserIdListInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> UserIdListInput:
    out: UserIdListInput = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: UserIdListInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> UserIdListInput:
    out: UserIdListInput = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
