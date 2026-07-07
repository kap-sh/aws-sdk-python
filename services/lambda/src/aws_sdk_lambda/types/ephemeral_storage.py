"""Generated from Smithy shape ``com.amazonaws.lambda#EphemeralStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.ephemeral_storage_size


class EphemeralStorage(TypedDict, closed=True):
    size: "aws_sdk_lambda.types.ephemeral_storage_size.EphemeralStorageSize"
    """<p>The size of the function's <code>/tmp</code> directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralStorage) -> dict:
    out: dict = {}
    out["Size"] = value["size"]
    return out


def deserialize_json(data: dict) -> EphemeralStorage:
    out: EphemeralStorage = {}  # type: ignore[typeddict-item]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        raise DeserializationError("EphemeralStorage.size required")
    return out
