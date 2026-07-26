"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDataError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.query_error_code
    import capo_sesv2.types.query_error_message
    import capo_sesv2.types.query_identifier


class MetricDataError(TypedDict, closed=True):
    id: NotRequired["capo_sesv2.types.query_identifier.QueryIdentifier"]
    """<p>The query identifier.</p>"""
    code: NotRequired["capo_sesv2.types.query_error_code.QueryErrorCode"]
    """<p>The query error code. Can be one of:</p> <ul> <li> <p> <code>INTERNAL_FAILURE</code> – Amazon SES has failed to process one of the queries.</p> </li> <li> <p> <code>ACCESS_DENIED</code> – You have insufficient access to retrieve metrics based on the given query.</p> </li> </ul>"""
    message: NotRequired["capo_sesv2.types.query_error_message.QueryErrorMessage"]
    """<p>The error message associated with the current query error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataError) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "code" in value:
        import capo_sesv2.types.query_error_code

        out["Code"] = capo_sesv2.types.query_error_code.serialize_json(value["code"])
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MetricDataError:
    out: MetricDataError = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Code" in data:
        import capo_sesv2.types.query_error_code

        out["code"] = capo_sesv2.types.query_error_code.deserialize_json(data["Code"])
    if "Message" in data:
        out["message"] = data["Message"]
    return out
