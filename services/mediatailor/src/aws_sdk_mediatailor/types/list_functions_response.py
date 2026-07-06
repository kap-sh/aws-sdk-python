"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_functions_response
    import aws_sdk_mediatailor.types.__string


class ListFunctionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_functions_response.__listOfFunctionsResponse"
    ]
    """<p>A list of functions associated with your account in the current Region.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediatailor.types.__list_of_functions_response

        out["Items"] = (
            aws_sdk_mediatailor.types.__list_of_functions_response.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFunctionsResponse:
    out: ListFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediatailor.types.__list_of_functions_response

        out["items"] = (
            aws_sdk_mediatailor.types.__list_of_functions_response.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
