"""Generated from Smithy shape ``com.amazonaws.elasticache#ProcessedUpdateActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.processed_update_action

ProcessedUpdateActionList: TypeAlias = list[
    "capo_elasticache.types.processed_update_action.ProcessedUpdateAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessedUpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.processed_update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.processed_update_action.serialize_query(
            item, pairs, f"{prefix}.ProcessedUpdateAction.{n}"
        )


def deserialize_query(el: Element) -> ProcessedUpdateActionList:
    import capo_elasticache.types.processed_update_action

    out: ProcessedUpdateActionList = []
    for child in el.findall("ProcessedUpdateAction"):
        out.append(
            capo_elasticache.types.processed_update_action.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ProcessedUpdateActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.processed_update_action

    for n, item in enumerate(value, 1):
        capo_elasticache.types.processed_update_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ProcessedUpdateActionList:
    import capo_elasticache.types.processed_update_action

    out: ProcessedUpdateActionList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.processed_update_action.deserialize_query(child)
        )
    return out
