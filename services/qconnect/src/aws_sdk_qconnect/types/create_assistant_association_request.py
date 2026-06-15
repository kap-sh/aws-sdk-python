"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAssistantAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_association_input_data
    import aws_sdk_qconnect.types.association_type
    import aws_sdk_qconnect.types.client_token
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid_or_arn


class CreateAssistantAssociationRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    association_type: "aws_sdk_qconnect.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association: "aws_sdk_qconnect.types.assistant_association_input_data.AssistantAssociationInputData"
    """<p>The identifier of the associated resource.</p>"""
    client_token: NotRequired["aws_sdk_qconnect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantAssociationRequest) -> dict:
    out: dict = {}
    out["associationType"] = value["association_type"]
    import aws_sdk_qconnect.types.assistant_association_input_data

    out["association"] = (
        aws_sdk_qconnect.types.assistant_association_input_data.serialize_json(
            value["association"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssistantAssociationRequest:
    out: CreateAssistantAssociationRequest = {}  # type: ignore[typeddict-item]
    if "associationType" in data:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError(
            "CreateAssistantAssociationRequest.association_type required"
        )
    if "association" in data:
        import aws_sdk_qconnect.types.assistant_association_input_data

        out["association"] = (
            aws_sdk_qconnect.types.assistant_association_input_data.deserialize_json(
                data["association"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssistantAssociationRequest.association required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
