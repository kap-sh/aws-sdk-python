"""Generated from Smithy shape ``com.amazonaws.rds#RecommendedActionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.recommended_action

RecommendedActionList: TypeAlias = list[
    "capo_rds.types.recommended_action.RecommendedAction"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendedActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.recommended_action

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.recommended_action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RecommendedActionList:
    import capo_rds.types.recommended_action

    out: RecommendedActionList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.recommended_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecommendedActionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.recommended_action

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.recommended_action.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RecommendedActionList:
    import capo_rds.types.recommended_action

    out: RecommendedActionList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.recommended_action.deserialize_query(child))
    return out
