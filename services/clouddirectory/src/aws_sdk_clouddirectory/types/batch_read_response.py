"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_read_operation_response_list


class BatchReadResponse(TypedDict, closed=True):
    responses: NotRequired[
        "aws_sdk_clouddirectory.types.batch_read_operation_response_list.BatchReadOperationResponseList"
    ]
    """<p>A list of all the responses for each batch read.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadResponse) -> dict:
    out: dict = {}
    if "responses" in value:
        import aws_sdk_clouddirectory.types.batch_read_operation_response_list

        out["Responses"] = (
            aws_sdk_clouddirectory.types.batch_read_operation_response_list.serialize_json(
                value["responses"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchReadResponse:
    out: BatchReadResponse = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import aws_sdk_clouddirectory.types.batch_read_operation_response_list

        out["responses"] = (
            aws_sdk_clouddirectory.types.batch_read_operation_response_list.deserialize_json(
                data["Responses"]
            )
        )
    return out
