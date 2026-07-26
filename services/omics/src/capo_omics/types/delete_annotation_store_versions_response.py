"""Generated from Smithy shape ``com.amazonaws.omics#DeleteAnnotationStoreVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.version_delete_error_list


class DeleteAnnotationStoreVersionsResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_omics.types.version_delete_error_list.VersionDeleteErrorList"
    ]
    """<p> Any errors that occur when attempting to delete an annotation store version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnnotationStoreVersionsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_omics.types.version_delete_error_list

        out["errors"] = capo_omics.types.version_delete_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> DeleteAnnotationStoreVersionsResponse:
    out: DeleteAnnotationStoreVersionsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_omics.types.version_delete_error_list

        out["errors"] = capo_omics.types.version_delete_error_list.deserialize_json(
            data["errors"]
        )
    return out
