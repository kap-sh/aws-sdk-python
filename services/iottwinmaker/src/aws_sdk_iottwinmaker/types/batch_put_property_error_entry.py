"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyErrorEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.errors


class BatchPutPropertyErrorEntry(TypedDict):
    errors: "aws_sdk_iottwinmaker.types.errors.Errors"
    """<p>A list of objects that contain information about errors returned by the <code>BatchPutProperty</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyErrorEntry) -> dict:
    out: dict = {}
    import aws_sdk_iottwinmaker.types.errors

    out["errors"] = aws_sdk_iottwinmaker.types.errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchPutPropertyErrorEntry:
    out: BatchPutPropertyErrorEntry = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_iottwinmaker.types.errors

        out["errors"] = aws_sdk_iottwinmaker.types.errors.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchPutPropertyErrorEntry.errors required")
    return out
