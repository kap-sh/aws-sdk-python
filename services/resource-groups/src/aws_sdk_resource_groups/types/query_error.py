"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.query_error_code
    import aws_sdk_resource_groups.types.query_error_message


class QueryError(TypedDict):
    error_code: NotRequired[
        "aws_sdk_resource_groups.types.query_error_code.QueryErrorCode"
    ]
    """<p>Specifies the error code that was raised.</p>"""
    message: NotRequired[
        "aws_sdk_resource_groups.types.query_error_message.QueryErrorMessage"
    ]
    """<p>A message that explains the <code>ErrorCode</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_resource_groups.types.query_error_code

        out["ErrorCode"] = (
            aws_sdk_resource_groups.types.query_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> QueryError:
    out: QueryError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_resource_groups.types.query_error_code

        out["error_code"] = (
            aws_sdk_resource_groups.types.query_error_code.deserialize_json(
                data["ErrorCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
