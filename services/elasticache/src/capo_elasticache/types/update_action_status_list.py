"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.update_action_status

UpdateActionStatusList: TypeAlias = list[
    "capo_elasticache.types.update_action_status.UpdateActionStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateActionStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.update_action_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.update_action_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UpdateActionStatusList:
    import capo_elasticache.types.update_action_status

    out: UpdateActionStatusList = []
    for child in el.findall("member"):
        out.append(capo_elasticache.types.update_action_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: UpdateActionStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.update_action_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.update_action_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UpdateActionStatusList:
    import capo_elasticache.types.update_action_status

    out: UpdateActionStatusList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.update_action_status.deserialize_query(child))
    return out
