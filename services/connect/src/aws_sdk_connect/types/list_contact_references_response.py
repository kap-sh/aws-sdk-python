"""Generated from Smithy shape ``com.amazonaws.connect#ListContactReferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.reference_summary_list


class ListContactReferencesResponse(TypedDict, closed=True):
    reference_summary_list: NotRequired[
        "aws_sdk_connect.types.reference_summary_list.ReferenceSummaryList"
    ]
    """<p>Information about the flows.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p> <important> <p>This is always returned as null in the response.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactReferencesResponse) -> dict:
    out: dict = {}
    if "reference_summary_list" in value:
        import aws_sdk_connect.types.reference_summary_list

        out["ReferenceSummaryList"] = (
            aws_sdk_connect.types.reference_summary_list.serialize_json(
                value["reference_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactReferencesResponse:
    out: ListContactReferencesResponse = {}  # type: ignore[typeddict-item]
    if "ReferenceSummaryList" in data:
        import aws_sdk_connect.types.reference_summary_list

        out["reference_summary_list"] = (
            aws_sdk_connect.types.reference_summary_list.deserialize_json(
                data["ReferenceSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
