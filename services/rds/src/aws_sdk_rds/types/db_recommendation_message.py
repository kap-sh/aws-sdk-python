"""Generated from Smithy shape ``com.amazonaws.rds#DBRecommendationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_recommendation


class DBRecommendationMessage(TypedDict, closed=True):
    db_recommendation: NotRequired[
        "aws_sdk_rds.types.db_recommendation.DBRecommendation"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBRecommendationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_recommendation" in value:
        import aws_sdk_rds.types.db_recommendation

        aws_sdk_rds.types.db_recommendation.serialize_query(
            value["db_recommendation"], pairs, f"{prefix}.DBRecommendation"
        )


def deserialize_query(el: Element) -> DBRecommendationMessage:
    out: DBRecommendationMessage = {}  # type: ignore[typeddict-item]
    child_db_recommendation = el.find("DBRecommendation")
    if child_db_recommendation is not None:
        import aws_sdk_rds.types.db_recommendation

        out["db_recommendation"] = (
            aws_sdk_rds.types.db_recommendation.deserialize_query(
                child_db_recommendation
            )
        )
    return out
