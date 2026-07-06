"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PathToObjectIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier_list
    import aws_sdk_clouddirectory.types.path_string


class PathToObjectIdentifiers(TypedDict, closed=True):
    path: NotRequired["aws_sdk_clouddirectory.types.path_string.PathString"]
    """<p>The path that is used to identify the object starting from directory root.</p>"""
    object_identifiers: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier_list.ObjectIdentifierList"
    ]
    """<p>Lists <code>ObjectIdentifiers</code> starting from directory root to the object in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathToObjectIdentifiers) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "object_identifiers" in value:
        import aws_sdk_clouddirectory.types.object_identifier_list

        out["ObjectIdentifiers"] = (
            aws_sdk_clouddirectory.types.object_identifier_list.serialize_json(
                value["object_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> PathToObjectIdentifiers:
    out: PathToObjectIdentifiers = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "ObjectIdentifiers" in data:
        import aws_sdk_clouddirectory.types.object_identifier_list

        out["object_identifiers"] = (
            aws_sdk_clouddirectory.types.object_identifier_list.deserialize_json(
                data["ObjectIdentifiers"]
            )
        )
    return out
