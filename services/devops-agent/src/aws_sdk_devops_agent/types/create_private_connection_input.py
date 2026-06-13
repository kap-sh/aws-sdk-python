"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreatePrivateConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_mode
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.tags


class CreatePrivateConnectionInput(TypedDict):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>Unique name for this Private Connection within the account.</p>"""
    mode: "aws_sdk_devops_agent.types.private_connection_mode.PrivateConnectionMode"
    """<p>Private Connection mode configuration.</p>"""
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the Private Connection at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateConnectionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_devops_agent.types.private_connection_mode

    out["mode"] = aws_sdk_devops_agent.types.private_connection_mode.serialize_json(
        value["mode"]
    )
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePrivateConnectionInput:
    out: CreatePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePrivateConnectionInput.name required")
    if "mode" in data:
        import aws_sdk_devops_agent.types.private_connection_mode

        out["mode"] = (
            aws_sdk_devops_agent.types.private_connection_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        raise DeserializationError("CreatePrivateConnectionInput.mode required")
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
