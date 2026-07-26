"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedNamedQueryId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.error_code
    import capo_athena.types.error_message
    import capo_athena.types.named_query_id


class UnprocessedNamedQueryId(TypedDict, closed=True):
    named_query_id: NotRequired["capo_athena.types.named_query_id.NamedQueryId"]
    """<p>The unique identifier of the named query.</p>"""
    error_code: NotRequired["capo_athena.types.error_code.ErrorCode"]
    """<p>The error code returned when the processing request for the named query failed, if applicable.</p>"""
    error_message: NotRequired["capo_athena.types.error_message.ErrorMessage"]
    """<p>The error message returned when the processing request for the named query failed, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedNamedQueryId) -> dict:
    out: dict = {}
    if "named_query_id" in value:
        out["NamedQueryId"] = value["named_query_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedNamedQueryId:
    out: UnprocessedNamedQueryId = {}  # type: ignore[typeddict-item]
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
