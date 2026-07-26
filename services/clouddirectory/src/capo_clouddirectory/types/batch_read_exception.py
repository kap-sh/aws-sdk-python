"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_read_exception_type
    import capo_clouddirectory.types.exception_message


class BatchReadException(TypedDict, closed=True):
    type: NotRequired[
        "capo_clouddirectory.types.batch_read_exception_type.BatchReadExceptionType"
    ]
    """<p>A type of exception, such as <code>InvalidArnException</code>.</p>"""
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]
    """<p>An exception message that is associated with the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadException) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_clouddirectory.types.batch_read_exception_type

        out["Type"] = (
            capo_clouddirectory.types.batch_read_exception_type.serialize_json(
                value["type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchReadException:
    out: BatchReadException = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_clouddirectory.types.batch_read_exception_type

        out["type"] = (
            capo_clouddirectory.types.batch_read_exception_type.deserialize_json(
                data["Type"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
