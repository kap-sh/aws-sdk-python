"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCasesForContactResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_summary_list
    import aws_sdk_connectcases.types.next_token


class ListCasesForContactResponse(TypedDict):
    cases: "aws_sdk_connectcases.types.case_summary_list.CaseSummaryList"
    """<p>A list of Case summary information.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesForContactResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.case_summary_list

    out["cases"] = aws_sdk_connectcases.types.case_summary_list.serialize_json(
        value["cases"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCasesForContactResponse:
    out: ListCasesForContactResponse = {}  # type: ignore[typeddict-item]
    if "cases" in data:
        import aws_sdk_connectcases.types.case_summary_list

        out["cases"] = aws_sdk_connectcases.types.case_summary_list.deserialize_json(
            data["cases"]
        )
    else:
        raise DeserializationError("ListCasesForContactResponse.cases required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
