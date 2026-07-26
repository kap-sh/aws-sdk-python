"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeAlgorithmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.algorithm


class DescribeAlgorithmResponse(TypedDict, closed=True):
    algorithm: NotRequired["capo_personalize.types.algorithm.Algorithm"]
    """<p>A listing of the properties of the algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAlgorithmResponse) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import capo_personalize.types.algorithm

        out["algorithm"] = capo_personalize.types.algorithm.serialize_aws_json_1_1(
            value["algorithm"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAlgorithmResponse:
    out: DescribeAlgorithmResponse = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import capo_personalize.types.algorithm

        out["algorithm"] = capo_personalize.types.algorithm.deserialize_aws_json_1_1(
            data["algorithm"]
        )
    return out
