"""Generated from Smithy shape ``com.amazonaws.macie2#BatchGetCustomDataIdentifiersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string


class BatchGetCustomDataIdentifiersRequest(TypedDict):
    ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array of custom data identifier IDs, one for each custom data identifier to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCustomDataIdentifiersRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["ids"] = aws_sdk_macie2.types.__list_of__string.serialize_json(value["ids"])
    return out


def deserialize_json(data: dict) -> BatchGetCustomDataIdentifiersRequest:
    out: BatchGetCustomDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["ids"]
        )
    return out
