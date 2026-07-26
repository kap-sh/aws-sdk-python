"""Generated from Smithy shape ``com.amazonaws.redshift#RecommendedActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.recommended_action

RecommendedActionList: TypeAlias = list[
    "capo_redshift.types.recommended_action.RecommendedAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.recommended_action

    for n, item in enumerate(value, 1):
        capo_redshift.types.recommended_action.serialize_query(
            item, pairs, f"{prefix}.RecommendedAction.{n}"
        )


def deserialize_query(el: Element) -> RecommendedActionList:
    import capo_redshift.types.recommended_action

    out: RecommendedActionList = []
    for child in el.findall("RecommendedAction"):
        out.append(capo_redshift.types.recommended_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecommendedActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.recommended_action

    for n, item in enumerate(value, 1):
        capo_redshift.types.recommended_action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RecommendedActionList:
    import capo_redshift.types.recommended_action

    out: RecommendedActionList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.recommended_action.deserialize_query(child))
    return out
