"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.update_action

UpdateActionList: TypeAlias = list["capo_elasticache.types.update_action.UpdateAction"]


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.update_action.serialize_query(
            item, pairs, f"{prefix}.UpdateAction.{n}"
        )


def deserialize_query(el: Element) -> UpdateActionList:
    import capo_elasticache.types.update_action

    out: UpdateActionList = []
    for child in el.findall("UpdateAction"):
        out.append(capo_elasticache.types.update_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.update_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UpdateActionList:
    import capo_elasticache.types.update_action

    out: UpdateActionList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.update_action.deserialize_query(child))
    return out
