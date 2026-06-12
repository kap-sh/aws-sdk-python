"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyValuesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.error_entries


class BatchPutPropertyValuesResponse(TypedDict):
    error_entries: "aws_sdk_iottwinmaker.types.error_entries.ErrorEntries"
    """<p>Entries that caused errors in the batch put operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyValuesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.error_entries

    out["errorEntries"] = aws_sdk_iottwinmaker.types.error_entries.serialize_json(
        value["error_entries"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutPropertyValuesResponse:
    out: BatchPutPropertyValuesResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import aws_sdk_iottwinmaker.types.error_entries

        out["error_entries"] = (
            aws_sdk_iottwinmaker.types.error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutPropertyValuesResponse.error_entries required"
        )
    return out
