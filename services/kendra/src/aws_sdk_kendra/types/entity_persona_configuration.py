"""Generated from Smithy shape ``com.amazonaws.kendra#EntityPersonaConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_id
    import aws_sdk_kendra.types.persona


class EntityPersonaConfiguration(TypedDict):
    entity_id: "aws_sdk_kendra.types.entity_id.EntityId"
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    persona: "aws_sdk_kendra.types.persona.Persona"
    r"""<p>The persona that defines the specific permissions of the user or group in your IAM Identity Center identity source. The available personas or access roles are <code>Owner</code> and <code>Viewer</code>. For more information on these personas, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html#access-search-experience\">Providing access to your search page</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityPersonaConfiguration) -> dict:
    out: dict = {}
    out["EntityId"] = value["entity_id"]
    import aws_sdk_kendra.types.persona

    out["Persona"] = aws_sdk_kendra.types.persona.serialize_aws_json_1_1(
        value["persona"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityPersonaConfiguration:
    out: EntityPersonaConfiguration = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("EntityPersonaConfiguration.entity_id required")
    if "Persona" in data:
        import aws_sdk_kendra.types.persona

        out["persona"] = aws_sdk_kendra.types.persona.deserialize_aws_json_1_1(
            data["Persona"]
        )
    else:
        raise DeserializationError("EntityPersonaConfiguration.persona required")
    return out
