"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_interaction_type


class EvaluationFormTargetConfiguration(TypedDict, closed=True):
    contact_interaction_type: (
        "aws_sdk_connect.types.contact_interaction_type.ContactInteractionType"
    )
    """<p>The contact interaction type for this evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormTargetConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.contact_interaction_type

    out["ContactInteractionType"] = (
        aws_sdk_connect.types.contact_interaction_type.serialize_json(
            value["contact_interaction_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormTargetConfiguration:
    out: EvaluationFormTargetConfiguration = {}  # type: ignore[typeddict-item]
    if "ContactInteractionType" in data:
        import aws_sdk_connect.types.contact_interaction_type

        out["contact_interaction_type"] = (
            aws_sdk_connect.types.contact_interaction_type.deserialize_json(
                data["ContactInteractionType"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormTargetConfiguration.contact_interaction_type required"
        )
    return out
