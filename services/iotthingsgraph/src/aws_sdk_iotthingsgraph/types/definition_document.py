"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DefinitionDocument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.definition_language
    import aws_sdk_iotthingsgraph.types.definition_text


class DefinitionDocument(TypedDict):
    language: "aws_sdk_iotthingsgraph.types.definition_language.DefinitionLanguage"
    """<p>The language used to define the entity. <code>GRAPHQL</code> is the only valid value.</p>"""
    text: "aws_sdk_iotthingsgraph.types.definition_text.DefinitionText"
    """<p>The GraphQL text that defines the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefinitionDocument) -> dict:
    out: dict = {}
    import aws_sdk_iotthingsgraph.types.definition_language

    out["language"] = (
        aws_sdk_iotthingsgraph.types.definition_language.serialize_aws_json_1_1(
            value["language"]
        )
    )
    out["text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DefinitionDocument:
    out: DefinitionDocument = {}  # type: ignore[typeddict-item]
    if "language" in data:
        import aws_sdk_iotthingsgraph.types.definition_language

        out["language"] = (
            aws_sdk_iotthingsgraph.types.definition_language.deserialize_aws_json_1_1(
                data["language"]
            )
        )
    else:
        raise DeserializationError("DefinitionDocument.language required")
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("DefinitionDocument.text required")
    return out
