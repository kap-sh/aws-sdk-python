"""Generated from Smithy shape ``com.amazonaws.elasticache#UnprocessedUpdateActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.unprocessed_update_action

UnprocessedUpdateActionList: TypeAlias = list[
    "capo_elasticache.types.unprocessed_update_action.UnprocessedUpdateAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UnprocessedUpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.unprocessed_update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.unprocessed_update_action.serialize_query(
            item, pairs, f"{prefix}.UnprocessedUpdateAction.{n}"
        )


def deserialize_query(el: Element) -> UnprocessedUpdateActionList:
    import capo_elasticache.types.unprocessed_update_action

    out: UnprocessedUpdateActionList = []
    for child in el.findall("UnprocessedUpdateAction"):
        out.append(
            capo_elasticache.types.unprocessed_update_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: UnprocessedUpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.unprocessed_update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.unprocessed_update_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UnprocessedUpdateActionList:
    import capo_elasticache.types.unprocessed_update_action

    out: UnprocessedUpdateActionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.unprocessed_update_action.deserialize_query(child)
        )
    return out
