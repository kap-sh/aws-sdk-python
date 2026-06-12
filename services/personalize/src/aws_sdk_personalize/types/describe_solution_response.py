"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSolutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.solution


class DescribeSolutionResponse(TypedDict):
    solution: NotRequired["aws_sdk_personalize.types.solution.Solution"]
    """<p>An object that describes the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSolutionResponse) -> dict:
    out: dict = {}
    if "solution" in value:
        import aws_sdk_personalize.types.solution

        out["solution"] = aws_sdk_personalize.types.solution.serialize_aws_json_1_1(
            value["solution"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSolutionResponse:
    out: DescribeSolutionResponse = {}  # type: ignore[typeddict-item]
    if "solution" in data:
        import aws_sdk_personalize.types.solution

        out["solution"] = aws_sdk_personalize.types.solution.deserialize_aws_json_1_1(
            data["solution"]
        )
    return out
