"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.recommender


class DescribeRecommenderResponse(TypedDict, closed=True):
    recommender: NotRequired["aws_sdk_personalize.types.recommender.Recommender"]
    """<p>The properties of the recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRecommenderResponse) -> dict:
    out: dict = {}
    if "recommender" in value:
        import aws_sdk_personalize.types.recommender

        out["recommender"] = (
            aws_sdk_personalize.types.recommender.serialize_aws_json_1_1(
                value["recommender"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRecommenderResponse:
    out: DescribeRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "recommender" in data:
        import aws_sdk_personalize.types.recommender

        out["recommender"] = (
            aws_sdk_personalize.types.recommender.deserialize_aws_json_1_1(
                data["recommender"]
            )
        )
    return out
