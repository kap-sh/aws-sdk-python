"""Generated from Smithy shape ``com.amazonaws.qconnect#DataReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_reference
    import aws_sdk_qconnect.types.generative_reference
    import aws_sdk_qconnect.types.suggested_message_reference


class _DataReference_contentReference(TypedDict, closed=True):
    contentReference: "aws_sdk_qconnect.types.content_reference.ContentReference"


class _DataReference_generativeReference(TypedDict, closed=True):
    generativeReference: (
        "aws_sdk_qconnect.types.generative_reference.GenerativeReference"
    )


class _DataReference_suggestedMessageReference(TypedDict, closed=True):
    suggestedMessageReference: (
        "aws_sdk_qconnect.types.suggested_message_reference.SuggestedMessageReference"
    )


DataReference: TypeAlias = (
    _DataReference_contentReference
    | _DataReference_generativeReference
    | _DataReference_suggestedMessageReference
)


# --- restJson1 ser/de ---
def serialize_json(value: DataReference) -> dict:
    if "contentReference" in value:
        import aws_sdk_qconnect.types.content_reference

        return {
            "contentReference": aws_sdk_qconnect.types.content_reference.serialize_json(
                value["contentReference"]
            )
        }
    elif "generativeReference" in value:
        import aws_sdk_qconnect.types.generative_reference

        return {
            "generativeReference": aws_sdk_qconnect.types.generative_reference.serialize_json(
                value["generativeReference"]
            )
        }
    elif "suggestedMessageReference" in value:
        import aws_sdk_qconnect.types.suggested_message_reference

        return {
            "suggestedMessageReference": aws_sdk_qconnect.types.suggested_message_reference.serialize_json(
                value["suggestedMessageReference"]
            )
        }
    else:
        raise SerializationError("DataReference: no variant present")


def deserialize_json(data: dict) -> DataReference:
    if "contentReference" in data:
        import aws_sdk_qconnect.types.content_reference

        return {
            "contentReference": aws_sdk_qconnect.types.content_reference.deserialize_json(
                data["contentReference"]
            )
        }
    elif "generativeReference" in data:
        import aws_sdk_qconnect.types.generative_reference

        return {
            "generativeReference": aws_sdk_qconnect.types.generative_reference.deserialize_json(
                data["generativeReference"]
            )
        }
    elif "suggestedMessageReference" in data:
        import aws_sdk_qconnect.types.suggested_message_reference

        return {
            "suggestedMessageReference": aws_sdk_qconnect.types.suggested_message_reference.deserialize_json(
                data["suggestedMessageReference"]
            )
        }
    else:
        raise DeserializationError("DataReference: no recognized variant key")
