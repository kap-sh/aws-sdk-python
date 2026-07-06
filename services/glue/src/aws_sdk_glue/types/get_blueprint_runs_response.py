"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_runs
    import aws_sdk_glue.types.generic_string


class GetBlueprintRunsResponse(TypedDict, closed=True):
    blueprint_runs: NotRequired["aws_sdk_glue.types.blueprint_runs.BlueprintRuns"]
    """<p>Returns a list of <code>BlueprintRun</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all blueprint runs have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRunsResponse) -> dict:
    out: dict = {}
    if "blueprint_runs" in value:
        import aws_sdk_glue.types.blueprint_runs

        out["BlueprintRuns"] = aws_sdk_glue.types.blueprint_runs.serialize_aws_json_1_1(
            value["blueprint_runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRunsResponse:
    out: GetBlueprintRunsResponse = {}  # type: ignore[typeddict-item]
    if "BlueprintRuns" in data:
        import aws_sdk_glue.types.blueprint_runs

        out["blueprint_runs"] = (
            aws_sdk_glue.types.blueprint_runs.deserialize_aws_json_1_1(
                data["BlueprintRuns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
