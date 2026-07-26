"""Generated from Smithy shape ``com.amazonaws.wisdom#SessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.description
    import capo_wisdom.types.name
    import capo_wisdom.types.session_integration_configuration
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class SessionData(TypedDict, closed=True):
    session_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the session.</p>"""
    description: NotRequired["capo_wisdom.types.description.Description"]
    """<p>The description of the session.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    integration_configuration: NotRequired[
        "capo_wisdom.types.session_integration_configuration.SessionIntegrationConfiguration"
    ]
    """<p>The configuration information for the session integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionData) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["sessionId"] = value["session_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    if "integration_configuration" in value:
        import capo_wisdom.types.session_integration_configuration

        out["integrationConfiguration"] = (
            capo_wisdom.types.session_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionData:
    out: SessionData = {}  # type: ignore[typeddict-item]
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("SessionData.session_arn required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionData.session_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SessionData.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    if "integrationConfiguration" in data:
        import capo_wisdom.types.session_integration_configuration

        out["integration_configuration"] = (
            capo_wisdom.types.session_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    return out
