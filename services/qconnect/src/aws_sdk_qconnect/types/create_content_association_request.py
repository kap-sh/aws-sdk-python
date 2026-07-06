"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateContentAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.content_association_contents
    import aws_sdk_qconnect.types.content_association_type
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid_or_arn


class CreateContentAssociationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base.</p>"""
    content_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content.</p>"""
    association_type: (
        "aws_sdk_qconnect.types.content_association_type.ContentAssociationType"
    )
    """<p>The type of association.</p>"""
    association: (
        "aws_sdk_qconnect.types.content_association_contents.ContentAssociationContents"
    )
    """<p>The identifier of the associated resource.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContentAssociationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["associationType"] = value["association_type"]
    import aws_sdk_qconnect.types.content_association_contents

    out["association"] = (
        aws_sdk_qconnect.types.content_association_contents.serialize_json(
            value["association"]
        )
    )
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateContentAssociationRequest:
    out: CreateContentAssociationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError(
            "CreateContentAssociationRequest.association_type required"
        )
    if "association" in data:
        import aws_sdk_qconnect.types.content_association_contents

        out["association"] = (
            aws_sdk_qconnect.types.content_association_contents.deserialize_json(
                data["association"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContentAssociationRequest.association required"
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
