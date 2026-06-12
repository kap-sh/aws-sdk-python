"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetQueryStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.error_message_string
    import aws_sdk_lakeformation.types.query_state_string


class GetQueryStateResponse(TypedDict):
    error: NotRequired[
        "aws_sdk_lakeformation.types.error_message_string.ErrorMessageString"
    ]
    """<p>An error message when the operation fails.</p>"""
    state: "aws_sdk_lakeformation.types.query_state_string.QueryStateString"
    """<p>The state of a query previously submitted. The possible states are:</p> <ul> <li> <p>PENDING: the query is pending.</p> </li> <li> <p>WORKUNITS_AVAILABLE: some work units are ready for retrieval and execution.</p> </li> <li> <p>FINISHED: the query planning finished successfully, and all work units are ready for retrieval and execution.</p> </li> <li> <p>ERROR: an error occurred with the query, such as an invalid query ID or a backend error.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStateResponse) -> dict:
    out: dict = {}
    if "error" in value:
        out["Error"] = value["error"]
    import aws_sdk_lakeformation.types.query_state_string

    out["State"] = aws_sdk_lakeformation.types.query_state_string.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> GetQueryStateResponse:
    out: GetQueryStateResponse = {}  # type: ignore[typeddict-item]
    if "Error" in data:
        out["error"] = data["Error"]
    if "State" in data:
        import aws_sdk_lakeformation.types.query_state_string

        out["state"] = aws_sdk_lakeformation.types.query_state_string.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("GetQueryStateResponse.state required")
    return out
