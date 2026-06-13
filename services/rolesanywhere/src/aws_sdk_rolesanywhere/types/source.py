"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#Source``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.source_data
    import aws_sdk_rolesanywhere.types.trust_anchor_type


class Source(TypedDict):
    source_type: NotRequired[
        "aws_sdk_rolesanywhere.types.trust_anchor_type.TrustAnchorType"
    ]
    """<p>The type of the trust anchor. </p>"""
    source_data: NotRequired["aws_sdk_rolesanywhere.types.source_data.SourceData"]
    """<p>The data field of the trust anchor depending on its type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    out: dict = {}
    if "source_type" in value:
        out["sourceType"] = value["source_type"]
    if "source_data" in value:
        import aws_sdk_rolesanywhere.types.source_data

        out["sourceData"] = aws_sdk_rolesanywhere.types.source_data.serialize_json(
            value["source_data"]
        )
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if "sourceType" in data:
        out["source_type"] = data["sourceType"]
    if "sourceData" in data:
        import aws_sdk_rolesanywhere.types.source_data

        out["source_data"] = aws_sdk_rolesanywhere.types.source_data.deserialize_json(
            data["sourceData"]
        )
    return out
