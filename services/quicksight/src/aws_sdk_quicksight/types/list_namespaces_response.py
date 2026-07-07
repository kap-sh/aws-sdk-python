"""Generated from Smithy shape ``com.amazonaws.quicksight#ListNamespacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.namespaces
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class ListNamespacesResponse(TypedDict, closed=True):
    namespaces: NotRequired["aws_sdk_quicksight.types.namespaces.Namespaces"]
    """<p>The information about the namespaces in this Amazon Web Services account. The response includes the namespace ARN, name, Amazon Web Services Region, notification email address, creation status, and identity store.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A unique pagination token that can be used in a subsequent request. Receiving <code>NextToken</code> in your response inticates that there is more data that can be returned. To receive the data, make another <code>ListNamespaces</code> API call with the returned token to retrieve the next page of data. Each token is valid for 24 hours. If you try to make a <code>ListNamespaces</code> API call with an expired token, you will receive a <code>HTTP 400 InvalidNextTokenException</code> error.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    if "namespaces" in value:
        import aws_sdk_quicksight.types.namespaces

        out["Namespaces"] = aws_sdk_quicksight.types.namespaces.serialize_json(
            value["namespaces"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if "Namespaces" in data:
        import aws_sdk_quicksight.types.namespaces

        out["namespaces"] = aws_sdk_quicksight.types.namespaces.deserialize_json(
            data["Namespaces"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
