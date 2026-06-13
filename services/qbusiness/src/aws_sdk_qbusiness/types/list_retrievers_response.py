"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListRetrieversResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.retrievers


class ListRetrieversResponse(TypedDict):
    retrievers: NotRequired["aws_sdk_qbusiness.types.retrievers.Retrievers"]
    """<p>An array of summary information for one or more retrievers.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of retrievers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRetrieversResponse) -> dict:
    out: dict = {}
    if "retrievers" in value:
        import aws_sdk_qbusiness.types.retrievers

        out["retrievers"] = aws_sdk_qbusiness.types.retrievers.serialize_json(
            value["retrievers"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRetrieversResponse:
    out: ListRetrieversResponse = {}  # type: ignore[typeddict-item]
    if "retrievers" in data:
        import aws_sdk_qbusiness.types.retrievers

        out["retrievers"] = aws_sdk_qbusiness.types.retrievers.deserialize_json(
            data["retrievers"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
