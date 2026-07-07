"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkInstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class GetSolNetworkInstanceMetadata(TypedDict, closed=True):
    created_at: "datetime.datetime"
    """<p>The date that the resource was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>The date that the resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkInstanceMetadata) -> dict:
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


def deserialize_json(data: dict) -> GetSolNetworkInstanceMetadata:
    out: GetSolNetworkInstanceMetadata = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["created_at"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSolNetworkInstanceMetadata.created_at required")
    if "lastModified" in data:
        import aws_sdk_tnb.types._prelude.timestamp

        out["last_modified"] = aws_sdk_tnb.types._prelude.timestamp.deserialize_json(
            data["lastModified"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkInstanceMetadata.last_modified required"
        )
    return out
