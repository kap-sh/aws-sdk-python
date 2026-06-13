"""Generated from Smithy shape ``com.amazonaws.wisdom#GetAssistantAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.assistant_association_data


class GetAssistantAssociationResponse(TypedDict):
    assistant_association: NotRequired[
        "aws_sdk_wisdom.types.assistant_association_data.AssistantAssociationData"
    ]
    """<p>The assistant association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssistantAssociationResponse) -> dict:
    out: dict = {}
    if "assistant_association" in value:
        import aws_sdk_wisdom.types.assistant_association_data

        out["assistantAssociation"] = (
            aws_sdk_wisdom.types.assistant_association_data.serialize_json(
                value["assistant_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssistantAssociationResponse:
    out: GetAssistantAssociationResponse = {}  # type: ignore[typeddict-item]
    if "assistantAssociation" in data:
        import aws_sdk_wisdom.types.assistant_association_data

        out["assistant_association"] = (
            aws_sdk_wisdom.types.assistant_association_data.deserialize_json(
                data["assistantAssociation"]
            )
        )
    return out
