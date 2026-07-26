"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionInstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class GetSolFunctionInstanceMetadata(TypedDict, closed=True):
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionInstanceMetadata) -> dict:
    out: dict = {}
    import capo_tnb.types._prelude.timestamp

    out["createdAt"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_tnb.types._prelude.timestamp

    out["lastModified"] = capo_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> GetSolFunctionInstanceMetadata:
    out: GetSolFunctionInstanceMetadata = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import capo_tnb.types._prelude.timestamp

        out["created_at"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolFunctionInstanceMetadata.created_at required")
    if "lastModified" in data:
        import capo_tnb.types._prelude.timestamp

        out["last_modified"] = capo_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolFunctionInstanceMetadata.last_modified required"
        )
    return out
