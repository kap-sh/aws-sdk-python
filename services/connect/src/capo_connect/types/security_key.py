"""Generated from Smithy shape ``com.amazonaws.connect#SecurityKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.association_id
    import capo_connect.types.pem
    import capo_connect.types.timestamp


class SecurityKey(TypedDict, closed=True):
    association_id: NotRequired["capo_connect.types.association_id.AssociationId"]
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    key: NotRequired["capo_connect.types.pem.PEM"]
    """<p>The key of the security key.</p>"""
    creation_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>When the security key was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityKey) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "key" in value:
        out["Key"] = value["key"]
    if "creation_time" in value:
        import capo_connect.types.timestamp

        out["CreationTime"] = capo_connect.types.timestamp.serialize_json(
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
        import capo_connect.types.timestamp

        out["creation_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
