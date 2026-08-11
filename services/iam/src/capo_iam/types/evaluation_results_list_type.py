"""Generated from Smithy shape ``com.amazonaws.iam#EvaluationResultsListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.evaluation_result

EvaluationResultsListType: TypeAlias = list[
    "capo_iam.types.evaluation_result.EvaluationResult"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationResultsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.evaluation_result

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.evaluation_result.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EvaluationResultsListType:
    import capo_iam.types.evaluation_result

    out: EvaluationResultsListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.evaluation_result.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EvaluationResultsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.evaluation_result

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.evaluation_result.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> EvaluationResultsListType:
    import capo_iam.types.evaluation_result

    out: EvaluationResultsListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.evaluation_result.deserialize_query(child))
    return out
