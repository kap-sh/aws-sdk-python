"""Generated from Smithy shape ``com.amazonaws.omics#ListSequenceStoresResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.sequence_store_detail_list


class ListSequenceStoresResponse(TypedDict):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    sequence_stores: (
        "aws_sdk_omics.types.sequence_store_detail_list.SequenceStoreDetailList"
    )
    """<p>A list of sequence stores.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSequenceStoresResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_omics.types.sequence_store_detail_list

    out["sequenceStores"] = (
        aws_sdk_omics.types.sequence_store_detail_list.serialize_json(
            value["sequence_stores"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSequenceStoresResponse:
    out: ListSequenceStoresResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sequenceStores" in data:
        import aws_sdk_omics.types.sequence_store_detail_list

        out["sequence_stores"] = (
            aws_sdk_omics.types.sequence_store_detail_list.deserialize_json(
                data["sequenceStores"]
            )
        )
    else:
        raise DeserializationError(
            "ListSequenceStoresResponse.sequence_stores required"
        )
    return out
