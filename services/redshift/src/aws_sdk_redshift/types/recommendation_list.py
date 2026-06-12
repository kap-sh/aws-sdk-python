"""Generated from Smithy shape ``com.amazonaws.redshift#RecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.recommendation

RecommendationList: TypeAlias = list[
    "aws_sdk_redshift.types.recommendation.Recommendation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.recommendation

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.recommendation.serialize_query(
            item, pairs, f"{prefix}.Recommendation.{n}"
        )


def deserialize_query(el: Element) -> RecommendationList:
    import aws_sdk_redshift.types.recommendation

    out: RecommendationList = []
    for child in el.findall("Recommendation"):
        out.append(aws_sdk_redshift.types.recommendation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RecommendationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.recommendation

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.recommendation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RecommendationList:
    import aws_sdk_redshift.types.recommendation

    out: RecommendationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.recommendation.deserialize_query(child))
    return out
