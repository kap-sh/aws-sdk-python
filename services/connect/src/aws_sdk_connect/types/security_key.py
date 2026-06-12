"""Generated from Smithy shape ``com.amazonaws.connect#SecurityKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.association_id
    import aws_sdk_connect.types.pem
    import aws_sdk_connect.types.timestamp


class SecurityKey(TypedDict):
    association_id: NotRequired["aws_sdk_connect.types.association_id.AssociationId"]
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    key: NotRequired["aws_sdk_connect.types.pem.PEM"]
    """<p>The key of the security key.</p>"""
    creation_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>When the security key was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityKey) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "key" in value:
        out["Key"] = value["key"]
    if "creation_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreationTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> SecurityKey:
    out: SecurityKey = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "Key" in data:
        out["key"] = data["Key"]
    if "CreationTime" in data:
        import aws_sdk_connect.types.timestamp

        out["creation_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
