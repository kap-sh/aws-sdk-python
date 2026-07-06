"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_read_exception
    import aws_sdk_clouddirectory.types.batch_read_successful_response


class BatchReadOperationResponse(TypedDict, closed=True):
    successful_response: NotRequired[
        "aws_sdk_clouddirectory.types.batch_read_successful_response.BatchReadSuccessfulResponse"
    ]
    """<p>Identifies which operation in a batch has succeeded.</p>"""
    exception_response: NotRequired[
        "aws_sdk_clouddirectory.types.batch_read_exception.BatchReadException"
    ]
    """<p>Identifies which operation in a batch has failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadOperationResponse) -> dict:
    out: dict = {}
    if "successful_response" in value:
        import aws_sdk_clouddirectory.types.batch_read_successful_response

        out["SuccessfulResponse"] = (
            aws_sdk_clouddirectory.types.batch_read_successful_response.serialize_json(
                value["successful_response"]
            )
        )
    if "exception_response" in value:
        import aws_sdk_clouddirectory.types.batch_read_exception

        out["ExceptionResponse"] = (
            aws_sdk_clouddirectory.types.batch_read_exception.serialize_json(
                value["exception_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchReadOperationResponse:
    out: BatchReadOperationResponse = {}  # type: ignore[typeddict-item]
    if "SuccessfulResponse" in data:
        import aws_sdk_clouddirectory.types.batch_read_successful_response

        out["successful_response"] = (
            aws_sdk_clouddirectory.types.batch_read_successful_response.deserialize_json(
                data["SuccessfulResponse"]
            )
        )
    if "ExceptionResponse" in data:
        import aws_sdk_clouddirectory.types.batch_read_exception

        out["exception_response"] = (
            aws_sdk_clouddirectory.types.batch_read_exception.deserialize_json(
                data["ExceptionResponse"]
            )
        )
    return out
