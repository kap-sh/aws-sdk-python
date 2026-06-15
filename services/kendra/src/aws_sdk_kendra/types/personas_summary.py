"""Generated from Smithy shape ``com.amazonaws.kendra#PersonasSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_id
    import aws_sdk_kendra.types.persona
    import aws_sdk_kendra.types.timestamp


class PersonasSummary(TypedDict):
    entity_id: NotRequired["aws_sdk_kendra.types.entity_id.EntityId"]
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    persona: NotRequired["aws_sdk_kendra.types.persona.Persona"]
    r"""<p>The persona that defines the specific permissions of the user or group in your IAM Identity Center identity source. The available personas or access roles are <code>Owner</code> and <code>Viewer</code>. For more information on these personas, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html#access-search-experience\">Providing access to your search page</a>.</p>"""
    created_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the summary information was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the summary information was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonasSummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "persona" in value:
        import aws_sdk_kendra.types.persona

        out["Persona"] = aws_sdk_kendra.types.persona.serialize_aws_json_1_1(
            value["persona"]
        )
    if "created_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["CreatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["UpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonasSummary:
    out: PersonasSummary = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "Persona" in data:
        import aws_sdk_kendra.types.persona

        out["persona"] = aws_sdk_kendra.types.persona.deserialize_aws_json_1_1(
            data["Persona"]
        )
    if "CreatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["created_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["updated_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
