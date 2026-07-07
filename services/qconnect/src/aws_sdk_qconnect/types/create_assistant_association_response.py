"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAssistantAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_association_data


class CreateAssistantAssociationResponse(TypedDict, closed=True):
    assistant_association: NotRequired[
        "aws_sdk_qconnect.types.assistant_association_data.AssistantAssociationData"
    ]
    """<p>The assistant association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantAssociationResponse) -> dict:
    out: dict = {}
    if "assistant_association" in value:
        import aws_sdk_qconnect.types.assistant_association_data

        out["assistantAssociation"] = (
            aws_sdk_qconnect.types.assistant_association_data.serialize_json(
                value["assistant_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssistantAssociationResponse:
    out: CreateAssistantAssociationResponse = {}  # type: ignore[typeddict-item]
    if "assistantAssociation" in data:
        import aws_sdk_qconnect.types.assistant_association_data

        out["assistant_association"] = (
            aws_sdk_qconnect.types.assistant_association_data.deserialize_json(
                data["assistantAssociation"]
            )
        )
    return out
