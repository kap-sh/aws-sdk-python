"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_summaries
    import aws_sdk_wellarchitected.types.next_token


class ListLensesOutput(TypedDict, closed=True):
    lens_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.lens_summaries.LensSummaries"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensesOutput) -> dict:
    out: dict = {}
    if "lens_summaries" in value:
        import aws_sdk_wellarchitected.types.lens_summaries

        out["LensSummaries"] = (
            aws_sdk_wellarchitected.types.lens_summaries.serialize_json(
                value["lens_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLensesOutput:
    out: ListLensesOutput = {}  # type: ignore[typeddict-item]
    if "LensSummaries" in data:
        import aws_sdk_wellarchitected.types.lens_summaries

        out["lens_summaries"] = (
            aws_sdk_wellarchitected.types.lens_summaries.deserialize_json(
                data["LensSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
