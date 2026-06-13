"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstanceMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ListSolFunctionInstanceMetadata(TypedDict):
    created_at: "datetime.datetime"
    """<p>When the network function instance was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>When the network function instance was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstanceMetadata) -> dict:
    out: dict = {}
    import aws_sdk_tnb.types._prelude.timestamp

    out["createdAt"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_tnb.types._prelude.timestamp

    out["lastModified"] = aws_sdk_tnb.types._prelude.timestamp.serialize_json(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> ListSolFunctionInstanceMetadata:
    out: ListSolFunctionInstanceMetadata = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["created_at"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "ListSolFunctionInstanceMetadata.created_at required"
        )
    if "lastModified" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["last_modified"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "ListSolFunctionInstanceMetadata.last_modified required"
        )
    return out
