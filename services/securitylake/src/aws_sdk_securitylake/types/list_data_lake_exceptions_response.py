"""Generated from Smithy shape ``com.amazonaws.securitylake#ListDataLakeExceptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_exception_list
    import aws_sdk_securitylake.types.next_token


class ListDataLakeExceptionsResponse(TypedDict):
    exceptions: NotRequired[
        "aws_sdk_securitylake.types.data_lake_exception_list.DataLakeExceptionList"
    ]
    """<p>Lists the failures that cannot be retried.</p>"""
    next_token: NotRequired["aws_sdk_securitylake.types.next_token.NextToken"]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeExceptionsResponse) -> dict:
    out: dict = {}
    if "exceptions" in value:
        import aws_sdk_securitylake.types.data_lake_exception_list

        out["exceptions"] = (
            aws_sdk_securitylake.types.data_lake_exception_list.serialize_json(
                value["exceptions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataLakeExceptionsResponse:
    out: ListDataLakeExceptionsResponse = {}  # type: ignore[typeddict-item]
    if "exceptions" in data:
        import aws_sdk_securitylake.types.data_lake_exception_list

        out["exceptions"] = (
            aws_sdk_securitylake.types.data_lake_exception_list.deserialize_json(
                data["exceptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
