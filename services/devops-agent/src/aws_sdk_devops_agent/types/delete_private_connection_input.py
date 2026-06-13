"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeletePrivateConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.private_connection_name


class DeletePrivateConnectionInput(TypedDict):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePrivateConnectionInput:
    out: DeletePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    return out
