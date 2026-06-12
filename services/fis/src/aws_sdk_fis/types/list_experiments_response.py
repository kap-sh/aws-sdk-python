"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_summary_list
    import aws_sdk_fis.types.next_token


class ListExperimentsResponse(TypedDict):
    experiments: NotRequired[
        "aws_sdk_fis.types.experiment_summary_list.ExperimentSummaryList"
    ]
    """<p>The experiments.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentsResponse) -> dict:
    out: dict = {}
    if "experiments" in value:
        import aws_sdk_fis.types.experiment_summary_list

        out["experiments"] = aws_sdk_fis.types.experiment_summary_list.serialize_json(
            value["experiments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExperimentsResponse:
    out: ListExperimentsResponse = {}  # type: ignore[typeddict-item]
    if "experiments" in data:
        import aws_sdk_fis.types.experiment_summary_list

        out["experiments"] = aws_sdk_fis.types.experiment_summary_list.deserialize_json(
            data["experiments"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
