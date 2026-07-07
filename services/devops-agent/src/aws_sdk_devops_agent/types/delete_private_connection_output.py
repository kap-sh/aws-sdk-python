"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeletePrivateConnectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.private_connection_status


class DeletePrivateConnectionOutput(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    status: (
        "aws_sdk_devops_agent.types.private_connection_status.PrivateConnectionStatus"
    )
    """<p>The status of the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateConnectionOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_devops_agent.types.private_connection_status

    out["status"] = aws_sdk_devops_agent.types.private_connection_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeletePrivateConnectionOutput:
    out: DeletePrivateConnectionOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeletePrivateConnectionOutput.name required")
    if "status" in data:
        import aws_sdk_devops_agent.types.private_connection_status

        out["status"] = (
            aws_sdk_devops_agent.types.private_connection_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeletePrivateConnectionOutput.status required")
    return out
