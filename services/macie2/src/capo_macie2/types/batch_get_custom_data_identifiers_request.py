"""Generated from Smithy shape ``com.amazonaws.macie2#BatchGetCustomDataIdentifiersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string


class BatchGetCustomDataIdentifiersRequest(TypedDict, closed=True):
    ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of custom data identifier IDs, one for each custom data identifier to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCustomDataIdentifiersRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_macie2.types.__list_of__string

        out["ids"] = capo_macie2.types.__list_of__string.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> BatchGetCustomDataIdentifiersRequest:
    out: BatchGetCustomDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import capo_macie2.types.__list_of__string

        out["ids"] = capo_macie2.types.__list_of__string.deserialize_json(data["ids"])
    return out
