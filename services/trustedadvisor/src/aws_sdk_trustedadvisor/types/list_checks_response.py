"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListChecksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.check_summary_list


class ListChecksResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    check_summaries: "aws_sdk_trustedadvisor.types.check_summary_list.CheckSummaryList"
    """<p>The list of Checks</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChecksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_trustedadvisor.types.check_summary_list

    out["checkSummaries"] = (
        aws_sdk_trustedadvisor.types.check_summary_list.serialize_json(
            value["check_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListChecksResponse:
    out: ListChecksResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "checkSummaries" in data:
        import aws_sdk_trustedadvisor.types.check_summary_list

        out["check_summaries"] = (
            aws_sdk_trustedadvisor.types.check_summary_list.deserialize_json(
                data["checkSummaries"]
            )
        )
    else:
        raise DeserializationError("ListChecksResponse.check_summaries required")
    return out
