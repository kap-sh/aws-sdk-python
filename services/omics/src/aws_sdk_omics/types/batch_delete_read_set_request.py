"""Generated from Smithy shape ``com.amazonaws.omics#BatchDeleteReadSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id_list
    import aws_sdk_omics.types.sequence_store_id


class BatchDeleteReadSetRequest(TypedDict):
    ids: "aws_sdk_omics.types.read_set_id_list.ReadSetIdList"
    """<p>The read sets' IDs.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read sets' sequence store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteReadSetRequest) -> dict:
    out: dict = {}
    import aws_sdk_omics.types.read_set_id_list

    out["ids"] = aws_sdk_omics.types.read_set_id_list.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteReadSetRequest:
    out: BatchDeleteReadSetRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_omics.types.read_set_id_list

        out["ids"] = aws_sdk_omics.types.read_set_id_list.deserialize_json(data["ids"])
    else:
        raise DeserializationError("BatchDeleteReadSetRequest.ids required")
    return out
