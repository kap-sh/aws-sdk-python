"""Generated from Smithy shape ``com.amazonaws.qconnect#ListSpansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.span_list


class ListSpansResponse(TypedDict, closed=True):
    spans: "aws_sdk_qconnect.types.span_list.SpanList"
    """<p>Array of span objects for the session</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>Pagination token for retrieving additional results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpansResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.span_list

    out["spans"] = aws_sdk_qconnect.types.span_list.serialize_json(value["spans"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSpansResponse:
    out: ListSpansResponse = {}  # type: ignore[typeddict-item]
    if "spans" in data:
        import aws_sdk_qconnect.types.span_list

        out["spans"] = aws_sdk_qconnect.types.span_list.deserialize_json(data["spans"])
    else:
        raise DeserializationError("ListSpansResponse.spans required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
