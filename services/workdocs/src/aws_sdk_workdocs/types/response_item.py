"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment_metadata
    import aws_sdk_workdocs.types.document_metadata
    import aws_sdk_workdocs.types.document_version_metadata
    import aws_sdk_workdocs.types.folder_metadata
    import aws_sdk_workdocs.types.response_item_type
    import aws_sdk_workdocs.types.response_item_web_url


class ResponseItem(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_workdocs.types.response_item_type.ResponseItemType"
    ]
    """<p>The type of item being returned.</p>"""
    web_url: NotRequired[
        "aws_sdk_workdocs.types.response_item_web_url.ResponseItemWebUrl"
    ]
    """<p>The webUrl of the item being returned.</p>"""
    document_metadata: NotRequired[
        "aws_sdk_workdocs.types.document_metadata.DocumentMetadata"
    ]
    """<p>The document that matches the query.</p>"""
    folder_metadata: NotRequired[
        "aws_sdk_workdocs.types.folder_metadata.FolderMetadata"
    ]
    """<p>The folder that matches the query.</p>"""
    comment_metadata: NotRequired[
        "aws_sdk_workdocs.types.comment_metadata.CommentMetadata"
    ]
    """<p>The comment that matches the query.</p>"""
    document_version_metadata: NotRequired[
        "aws_sdk_workdocs.types.document_version_metadata.DocumentVersionMetadata"
    ]
    """<p>The document version that matches the metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseItem) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_workdocs.types.response_item_type

        out["ResourceType"] = aws_sdk_workdocs.types.response_item_type.serialize_json(
            value["resource_type"]
        )
    if "web_url" in value:
        out["WebUrl"] = value["web_url"]
    if "document_metadata" in value:
        import aws_sdk_workdocs.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_workdocs.types.document_metadata.serialize_json(
                value["document_metadata"]
            )
        )
    if "folder_metadata" in value:
        import aws_sdk_workdocs.types.folder_metadata

        out["FolderMetadata"] = aws_sdk_workdocs.types.folder_metadata.serialize_json(
            value["folder_metadata"]
        )
    if "comment_metadata" in value:
        import aws_sdk_workdocs.types.comment_metadata

        out["CommentMetadata"] = aws_sdk_workdocs.types.comment_metadata.serialize_json(
            value["comment_metadata"]
        )
    if "document_version_metadata" in value:
        import aws_sdk_workdocs.types.document_version_metadata

        out["DocumentVersionMetadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.serialize_json(
                value["document_version_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResponseItem:
    out: ResponseItem = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_workdocs.types.response_item_type

        out["resource_type"] = (
            aws_sdk_workdocs.types.response_item_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "WebUrl" in data:
        out["web_url"] = data["WebUrl"]
    if "DocumentMetadata" in data:
        import aws_sdk_workdocs.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_workdocs.types.document_metadata.deserialize_json(
                data["DocumentMetadata"]
            )
        )
    if "FolderMetadata" in data:
        import aws_sdk_workdocs.types.folder_metadata

        out["folder_metadata"] = (
            aws_sdk_workdocs.types.folder_metadata.deserialize_json(
                data["FolderMetadata"]
            )
        )
    if "CommentMetadata" in data:
        import aws_sdk_workdocs.types.comment_metadata

        out["comment_metadata"] = (
            aws_sdk_workdocs.types.comment_metadata.deserialize_json(
                data["CommentMetadata"]
            )
        )
    if "DocumentVersionMetadata" in data:
        import aws_sdk_workdocs.types.document_version_metadata

        out["document_version_metadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.deserialize_json(
                data["DocumentVersionMetadata"]
            )
        )
    return out
