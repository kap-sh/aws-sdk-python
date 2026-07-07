"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeletedUniqueId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.header_safe_unique_id


class DeletedUniqueId(TypedDict, closed=True):
    unique_id: "aws_sdk_entityresolution.types.header_safe_unique_id.HeaderSafeUniqueId"
    """<p> The unique ID of the deleted item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletedUniqueId) -> dict:
    out: dict = {}
    out["uniqueId"] = value["unique_id"]
    return out


def deserialize_json(data: dict) -> DeletedUniqueId:
    out: DeletedUniqueId = {}  # type: ignore[typeddict-item]
    if "uniqueId" in data:
        out["unique_id"] = data["uniqueId"]
    else:
        raise DeserializationError("DeletedUniqueId.unique_id required")
    return out
