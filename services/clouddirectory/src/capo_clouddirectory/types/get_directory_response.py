"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetDirectoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.directory


class GetDirectoryResponse(TypedDict, closed=True):
    directory: "capo_clouddirectory.types.directory.Directory"
    """<p>Metadata about the directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectoryResponse) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.directory

    out["Directory"] = capo_clouddirectory.types.directory.serialize_json(
        value["directory"]
    )
    return out


def deserialize_json(data: dict) -> GetDirectoryResponse:
    out: GetDirectoryResponse = {}  # type: ignore[typeddict-item]
    if "Directory" in data:
        import capo_clouddirectory.types.directory

        out["directory"] = capo_clouddirectory.types.directory.deserialize_json(
            data["Directory"]
        )
    else:
        raise DeserializationError("GetDirectoryResponse.directory required")
    return out
