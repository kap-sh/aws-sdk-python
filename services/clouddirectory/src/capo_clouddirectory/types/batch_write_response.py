"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.batch_write_operation_response_list


class BatchWriteResponse(TypedDict, closed=True):
    responses: NotRequired[
        "capo_clouddirectory.types.batch_write_operation_response_list.BatchWriteOperationResponseList"
    ]
    """<p>A list of all the responses for each batch write.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteResponse) -> dict:
    out: dict = {}
    if "responses" in value:
        import capo_clouddirectory.types.batch_write_operation_response_list

        out["Responses"] = (
            capo_clouddirectory.types.batch_write_operation_response_list.serialize_json(
                value["responses"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchWriteResponse:
    out: BatchWriteResponse = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import capo_clouddirectory.types.batch_write_operation_response_list

        out["responses"] = (
            capo_clouddirectory.types.batch_write_operation_response_list.deserialize_json(
                data["Responses"]
            )
        )
    return out
