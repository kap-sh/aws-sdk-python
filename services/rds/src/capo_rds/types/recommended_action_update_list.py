"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedActionUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.recommended_action_update

RecommendedActionUpdateList: TypeAlias = list[
    "capo_rds.types.recommended_action_update.RecommendedActionUpdate"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.recommended_action_update

    for n, item in enumerate(value, 1):
        capo_rds.types.recommended_action_update.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RecommendedActionUpdateList:
    import capo_rds.types.recommended_action_update

    out: RecommendedActionUpdateList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.recommended_action_update.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecommendedActionUpdateList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.recommended_action_update

    for n, item in enumerate(value, 1):
        capo_rds.types.recommended_action_update.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RecommendedActionUpdateList:
    import capo_rds.types.recommended_action_update

    out: RecommendedActionUpdateList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.recommended_action_update.deserialize_query(child))
    return out
