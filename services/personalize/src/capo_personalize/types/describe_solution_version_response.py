"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSolutionVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.solution_version


class DescribeSolutionVersionResponse(TypedDict, closed=True):
    solution_version: NotRequired[
        "capo_personalize.types.solution_version.SolutionVersion"
    ]
    """<p>The solution version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSolutionVersionResponse) -> dict:
    out: dict = {}
    if "solution_version" in value:
        import capo_personalize.types.solution_version

        out["solutionVersion"] = (
            capo_personalize.types.solution_version.serialize_aws_json_1_1(
                value["solution_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSolutionVersionResponse:
    out: DescribeSolutionVersionResponse = {}  # type: ignore[typeddict-item]
    if "solutionVersion" in data:
        import capo_personalize.types.solution_version

        out["solution_version"] = (
            capo_personalize.types.solution_version.deserialize_aws_json_1_1(
                data["solutionVersion"]
            )
        )
    return out
