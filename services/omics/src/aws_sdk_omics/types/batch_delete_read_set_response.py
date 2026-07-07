"""Generated from Smithy shape ``com.amazonaws.omics#BatchDeleteReadSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_batch_error_list


class BatchDeleteReadSetResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_omics.types.read_set_batch_error_list.ReadSetBatchErrorList"
    ]
    """<p>Errors returned by individual delete operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteReadSetResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_omics.types.read_set_batch_error_list

        out["errors"] = aws_sdk_omics.types.read_set_batch_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteReadSetResponse:
    out: BatchDeleteReadSetResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_omics.types.read_set_batch_error_list

        out["errors"] = aws_sdk_omics.types.read_set_batch_error_list.deserialize_json(
            data["errors"]
        )
    return out
