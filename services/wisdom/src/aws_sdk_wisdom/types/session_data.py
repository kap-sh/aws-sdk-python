"""Generated from Smithy shape ``com.amazonaws.wisdom#SessionData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.description
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.session_integration_configuration
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid


class SessionData(TypedDict):
    session_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    name: "aws_sdk_wisdom.types.name.Name"
    """<p>The name of the session.</p>"""
    description: NotRequired["aws_sdk_wisdom.types.description.Description"]
    """<p>The description of the session.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    integration_configuration: NotRequired[
        "aws_sdk_wisdom.types.session_integration_configuration.SessionIntegrationConfiguration"
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
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    if "integration_configuration" in value:
        import aws_sdk_wisdom.types.session_integration_configuration

        out["integrationConfiguration"] = (
            aws_sdk_wisdom.types.session_integration_configuration.serialize_json(
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
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    if "integrationConfiguration" in data:
        import aws_sdk_wisdom.types.session_integration_configuration

        out["integration_configuration"] = (
            aws_sdk_wisdom.types.session_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    return out
