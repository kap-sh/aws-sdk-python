"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ExpressionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.expression_status

ExpressionStatusList: TypeAlias = list[
    "capo_cloudsearch.types.expression_status.ExpressionStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ExpressionStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.expression_status

    for n, item in enumerate(value, 1):
        capo_cloudsearch.types.expression_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ExpressionStatusList:
    import capo_cloudsearch.types.expression_status

    out: ExpressionStatusList = []
    for child in el.findall("member"):
        out.append(capo_cloudsearch.types.expression_status.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ExpressionStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.expression_status

    for n, item in enumerate(value, 1):
        capo_cloudsearch.types.expression_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ExpressionStatusList:
    import capo_cloudsearch.types.expression_status

    out: ExpressionStatusList = []
    for child in parent.findall(tag):
        out.append(capo_cloudsearch.types.expression_status.deserialize_query(child))
    return out
