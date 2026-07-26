"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeletePrivateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.private_connection_name


class DeletePrivateConnectionInput(TypedDict, closed=True):
    name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePrivateConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePrivateConnectionInput:
    out: DeletePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    return out
