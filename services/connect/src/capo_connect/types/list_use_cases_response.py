"""Generated from Smithy shape ``com.amazonaws.connect#ListUseCasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.use_case_summary_list


class ListUseCasesResponse(TypedDict, closed=True):
    use_case_summary_list: NotRequired[
        "capo_connect.types.use_case_summary_list.UseCaseSummaryList"
    ]
    """<p>The use cases.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUseCasesResponse) -> dict:
    out: dict = {}
    if "use_case_summary_list" in value:
        import capo_connect.types.use_case_summary_list

        out["UseCaseSummaryList"] = (
            capo_connect.types.use_case_summary_list.serialize_json(
                value["use_case_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUseCasesResponse:
    out: ListUseCasesResponse = {}  # type: ignore[typeddict-item]
    if "UseCaseSummaryList" in data:
        import capo_connect.types.use_case_summary_list

        out["use_case_summary_list"] = (
            capo_connect.types.use_case_summary_list.deserialize_json(
                data["UseCaseSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
