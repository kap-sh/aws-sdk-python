"""Generated from Smithy shape ``com.amazonaws.glacier#Grant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.grantee
    import capo_glacier.types.permission


class Grant(TypedDict, closed=True):
    grantee: NotRequired["capo_glacier.types.grantee.Grantee"]
    """<p>The grantee.</p>"""
    permission: NotRequired["capo_glacier.types.permission.Permission"]
    """<p>Specifies the permission given to the grantee. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Grant) -> dict:
    out: dict = {}
    if "grantee" in value:
        import capo_glacier.types.grantee

        out["Grantee"] = capo_glacier.types.grantee.serialize_json(value["grantee"])
    if "permission" in value:
        import capo_glacier.types.permission

        out["Permission"] = capo_glacier.types.permission.serialize_json(
            value["permission"]
        )
    return out


def deserialize_json(data: dict) -> Grant:
    out: Grant = {}  # type: ignore[typeddict-item]
    if "Grantee" in data:
        import capo_glacier.types.grantee

        out["grantee"] = capo_glacier.types.grantee.deserialize_json(data["Grantee"])
    if "Permission" in data:
        import capo_glacier.types.permission

        out["permission"] = capo_glacier.types.permission.deserialize_json(
            data["Permission"]
        )
    return out
