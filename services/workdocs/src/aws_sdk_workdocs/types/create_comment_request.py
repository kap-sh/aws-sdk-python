"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateCommentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.comment_id_type
    import aws_sdk_workdocs.types.comment_text_type
    import aws_sdk_workdocs.types.comment_visibility_type
    import aws_sdk_workdocs.types.document_version_id_type
    import aws_sdk_workdocs.types.resource_id_type


class CreateCommentRequest(TypedDict):
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the document.</p>"""
    version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
    """<p>The ID of the document version.</p>"""
    parent_id: NotRequired["aws_sdk_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the parent comment.</p>"""
    thread_id: NotRequired["aws_sdk_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the root comment in the thread.</p>"""
    text: "aws_sdk_workdocs.types.comment_text_type.CommentTextType"
    """<p>The text of the comment.</p>"""
    visibility: NotRequired[
        "aws_sdk_workdocs.types.comment_visibility_type.CommentVisibilityType"
    ]
    """<p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>"""
    notify_collaborators: "aws_sdk_workdocs.types.boolean_type.BooleanType"
    """<p>Set this parameter to TRUE to send an email out to the document collaborators after the comment is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommentRequest) -> dict:
    out: dict = {}
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "thread_id" in value:
        out["ThreadId"] = value["thread_id"]
    out["Text"] = value["text"]
    if "visibility" in value:
        import aws_sdk_workdocs.types.comment_visibility_type

        out["Visibility"] = (
            aws_sdk_workdocs.types.comment_visibility_type.serialize_json(
                value["visibility"]
            )
        )
    out["NotifyCollaborators"] = value.get("notify_collaborators", False)
    return out


def deserialize_json(data: dict) -> CreateCommentRequest:
    out: CreateCommentRequest = {}  # type: ignore[typeddict-item]
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    if "ThreadId" in data:
        out["thread_id"] = data["ThreadId"]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("CreateCommentRequest.text required")
    if "Visibility" in data:
        import aws_sdk_workdocs.types.comment_visibility_type

        out["visibility"] = (
            aws_sdk_workdocs.types.comment_visibility_type.deserialize_json(
                data["Visibility"]
            )
        )
    if "NotifyCollaborators" in data:
        out["notify_collaborators"] = data["NotifyCollaborators"]
    else:
        out["notify_collaborators"] = False
    return out
