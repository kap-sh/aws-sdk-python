"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeDocumentVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_version_metadata_list
    import capo_workdocs.types.page_marker_type


class DescribeDocumentVersionsResponse(TypedDict, closed=True):
    document_versions: NotRequired[
        "capo_workdocs.types.document_version_metadata_list.DocumentVersionMetadataList"
    ]
    """<p>The document versions.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDocumentVersionsResponse) -> dict:
    out: dict = {}
    if "document_versions" in value:
        import capo_workdocs.types.document_version_metadata_list

        out["DocumentVersions"] = (
            capo_workdocs.types.document_version_metadata_list.serialize_json(
                value["document_versions"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeDocumentVersionsResponse:
    out: DescribeDocumentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "DocumentVersions" in data:
        import capo_workdocs.types.document_version_metadata_list

        out["document_versions"] = (
            capo_workdocs.types.document_version_metadata_list.deserialize_json(
                data["DocumentVersions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
