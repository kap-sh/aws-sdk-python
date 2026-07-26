"""Generated from Smithy shape ``com.amazonaws.cognitosync#UpdateRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.record_list


class UpdateRecordsResponse(TypedDict, closed=True):
    records: NotRequired["capo_cognito_sync.types.record_list.RecordList"]
    """A list of records that have been updated."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecordsResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_cognito_sync.types.record_list

        out["Records"] = capo_cognito_sync.types.record_list.serialize_json(
            value["records"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRecordsResponse:
    out: UpdateRecordsResponse = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import capo_cognito_sync.types.record_list

        out["records"] = capo_cognito_sync.types.record_list.deserialize_json(
            data["Records"]
        )
    return out
