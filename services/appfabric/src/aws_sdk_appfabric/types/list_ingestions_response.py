"""Generated from Smithy shape ``com.amazonaws.appfabric#ListIngestionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.ingestion_list


class ListIngestionsResponse(TypedDict, closed=True):
    ingestions: "aws_sdk_appfabric.types.ingestion_list.IngestionList"
    """<p>Contains a list of ingestion summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_appfabric.types.ingestion_list

    out["ingestions"] = aws_sdk_appfabric.types.ingestion_list.serialize_json(
        value["ingestions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIngestionsResponse:
    out: ListIngestionsResponse = {}  # type: ignore[typeddict-item]
    if "ingestions" in data:
        import aws_sdk_appfabric.types.ingestion_list

        out["ingestions"] = aws_sdk_appfabric.types.ingestion_list.deserialize_json(
            data["ingestions"]
        )
    else:
        raise DeserializationError("ListIngestionsResponse.ingestions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
