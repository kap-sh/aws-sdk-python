"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.comment_metadata
    import capo_workdocs.types.document_metadata
    import capo_workdocs.types.document_version_metadata
    import capo_workdocs.types.folder_metadata
    import capo_workdocs.types.response_item_type
    import capo_workdocs.types.response_item_web_url


class ResponseItem(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_workdocs.types.response_item_type.ResponseItemType"
    ]
    """<p>The type of item being returned.</p>"""
    web_url: NotRequired["capo_workdocs.types.response_item_web_url.ResponseItemWebUrl"]
    """<p>The webUrl of the item being returned.</p>"""
    document_metadata: NotRequired[
        "capo_workdocs.types.document_metadata.DocumentMetadata"
    ]
    """<p>The document that matches the query.</p>"""
    folder_metadata: NotRequired["capo_workdocs.types.folder_metadata.FolderMetadata"]
    """<p>The folder that matches the query.</p>"""
    comment_metadata: NotRequired[
        "capo_workdocs.types.comment_metadata.CommentMetadata"
    ]
    """<p>The comment that matches the query.</p>"""
    document_version_metadata: NotRequired[
        "capo_workdocs.types.document_version_metadata.DocumentVersionMetadata"
    ]
    """<p>The document version that matches the metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseItem) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import capo_workdocs.types.response_item_type

        out["ResourceType"] = capo_workdocs.types.response_item_type.serialize_json(
            value["resource_type"]
        )
    if "web_url" in value:
        out["WebUrl"] = value["web_url"]
    if "document_metadata" in value:
        import capo_workdocs.types.document_metadata

        out["DocumentMetadata"] = capo_workdocs.types.document_metadata.serialize_json(
            value["document_metadata"]
        )
    if "folder_metadata" in value:
        import capo_workdocs.types.folder_metadata

        out["FolderMetadata"] = capo_workdocs.types.folder_metadata.serialize_json(
            value["folder_metadata"]
        )
    if "comment_metadata" in value:
        import capo_workdocs.types.comment_metadata

        out["CommentMetadata"] = capo_workdocs.types.comment_metadata.serialize_json(
            value["comment_metadata"]
        )
    if "document_version_metadata" in value:
        import capo_workdocs.types.document_version_metadata

        out["DocumentVersionMetadata"] = (
            capo_workdocs.types.document_version_metadata.serialize_json(
                value["document_version_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseItem:
    out: ResponseItem = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import capo_workdocs.types.response_item_type

        out["resource_type"] = capo_workdocs.types.response_item_type.deserialize_json(
            data["ResourceType"]
        )
    if "WebUrl" in data:
        out["web_url"] = data["WebUrl"]
    if "DocumentMetadata" in data:
        import capo_workdocs.types.document_metadata

        out["document_metadata"] = (
            capo_workdocs.types.document_metadata.deserialize_json(
                data["DocumentMetadata"]
            )
        )
    if "FolderMetadata" in data:
        import capo_workdocs.types.folder_metadata

        out["folder_metadata"] = capo_workdocs.types.folder_metadata.deserialize_json(
            data["FolderMetadata"]
        )
    if "CommentMetadata" in data:
        import capo_workdocs.types.comment_metadata

        out["comment_metadata"] = capo_workdocs.types.comment_metadata.deserialize_json(
            data["CommentMetadata"]
        )
    if "DocumentVersionMetadata" in data:
        import capo_workdocs.types.document_version_metadata

        out["document_version_metadata"] = (
            capo_workdocs.types.document_version_metadata.deserialize_json(
                data["DocumentVersionMetadata"]
            )
        )
    return out
