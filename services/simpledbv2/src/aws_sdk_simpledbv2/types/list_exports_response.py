"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ListExportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_simpledbv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.export_summaries
    import aws_sdk_simpledbv2.types.next_token


class ListExportsResponse(TypedDict):
    export_summaries: "aws_sdk_simpledbv2.types.export_summaries.ExportSummaries"
    """List of export summaries containing export ARN, status, request timestamp, and associated domain name."""
    next_token: NotRequired["aws_sdk_simpledbv2.types.next_token.NextToken"]
    """A pagination token indicating that more results are available. To retrieve the next page of results, provide this token in a subsequent ListExports request. If null or empty, there are no more results to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_simpledbv2.types.export_summaries

    out["exportSummaries"] = aws_sdk_simpledbv2.types.export_summaries.serialize_json(
        value["export_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportsResponse:
    out: ListExportsResponse = {}  # type: ignore[typeddict-item]
    if "exportSummaries" in data:
        import aws_sdk_simpledbv2.types.export_summaries

        out["export_summaries"] = (
            aws_sdk_simpledbv2.types.export_summaries.deserialize_json(
                data["exportSummaries"]
            )
        )
    else:
        raise DeserializationError("ListExportsResponse.export_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
