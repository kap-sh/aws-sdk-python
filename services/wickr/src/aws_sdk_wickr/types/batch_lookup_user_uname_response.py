"""Generated from Smithy shape ``com.amazonaws.wickr#BatchLookupUserUnameResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_uname_error_response_items
    import aws_sdk_wickr.types.batch_uname_success_response_items
    import aws_sdk_wickr.types.generic_string


class BatchLookupUserUnameResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch lookup operation.</p>"""
    successful: NotRequired[
        "aws_sdk_wickr.types.batch_uname_success_response_items.BatchUnameSuccessResponseItems"
    ]
    """<p>A list of successfully resolved username hashes with their corresponding email addresses.</p>"""
    failed: NotRequired[
        "aws_sdk_wickr.types.batch_uname_error_response_items.BatchUnameErrorResponseItems"
    ]
    """<p>A list of username hash lookup attempts that failed, including error details explaining why each lookup failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchLookupUserUnameResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import aws_sdk_wickr.types.batch_uname_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_uname_success_response_items.serialize_json(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_wickr.types.batch_uname_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_uname_error_response_items.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchLookupUserUnameResponse:
    out: BatchLookupUserUnameResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "successful" in data:
        import aws_sdk_wickr.types.batch_uname_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_uname_success_response_items.deserialize_json(
                data["successful"]
            )
        )
    if "failed" in data:
        import aws_sdk_wickr.types.batch_uname_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_uname_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out
