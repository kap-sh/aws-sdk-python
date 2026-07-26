"""Generated from Smithy shape ``com.amazonaws.s3files#RootDirectory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.creation_permissions
    import capo_s3files.types.path


class RootDirectory(TypedDict, closed=True):
    path: NotRequired["capo_s3files.types.path.Path"]
    """<p>The path to use as the root directory for the access point.</p>"""
    creation_permissions: NotRequired[
        "capo_s3files.types.creation_permissions.CreationPermissions"
    ]
    """<p>The permissions to set on newly created directories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RootDirectory) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "creation_permissions" in value:
        import capo_s3files.types.creation_permissions

        out["creationPermissions"] = (
            capo_s3files.types.creation_permissions.serialize_json(
                value["creation_permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RootDirectory:
    out: RootDirectory = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    if "creationPermissions" in data:
        import capo_s3files.types.creation_permissions

        out["creation_permissions"] = (
            capo_s3files.types.creation_permissions.deserialize_json(
                data["creationPermissions"]
            )
        )
    return out
