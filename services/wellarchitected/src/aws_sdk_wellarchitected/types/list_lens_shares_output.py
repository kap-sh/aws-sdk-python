"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensSharesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_share_summaries
    import aws_sdk_wellarchitected.types.next_token


class ListLensSharesOutput(TypedDict):
    lens_share_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.lens_share_summaries.LensShareSummaries"
    ]
    """<p>A list of lens share summaries.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensSharesOutput) -> dict:
    out: dict = {}
    if "lens_share_summaries" in value:
        import aws_sdk_wellarchitected.types.lens_share_summaries

        out["LensShareSummaries"] = (
            aws_sdk_wellarchitected.types.lens_share_summaries.serialize_json(
                value["lens_share_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLensSharesOutput:
    out: ListLensSharesOutput = {}  # type: ignore[typeddict-item]
    if "LensShareSummaries" in data:
        import aws_sdk_wellarchitected.types.lens_share_summaries

        out["lens_share_summaries"] = (
            aws_sdk_wellarchitected.types.lens_share_summaries.deserialize_json(
                data["LensShareSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
