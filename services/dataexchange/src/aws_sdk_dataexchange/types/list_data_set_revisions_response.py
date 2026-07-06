"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListDataSetRevisionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_revision_entry
    import aws_sdk_dataexchange.types.next_token


class ListDataSetRevisionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_dataexchange.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""
    revisions: NotRequired[
        "aws_sdk_dataexchange.types.list_of_revision_entry.ListOfRevisionEntry"
    ]
    """<p>The asset objects listed by the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetRevisionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "revisions" in value:
        import aws_sdk_dataexchange.types.list_of_revision_entry

        out["Revisions"] = (
            aws_sdk_dataexchange.types.list_of_revision_entry.serialize_json(
                value["revisions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataSetRevisionsResponse:
    out: ListDataSetRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Revisions" in data:
        import aws_sdk_dataexchange.types.list_of_revision_entry

        out["revisions"] = (
            aws_sdk_dataexchange.types.list_of_revision_entry.deserialize_json(
                data["Revisions"]
            )
        )
    return out
