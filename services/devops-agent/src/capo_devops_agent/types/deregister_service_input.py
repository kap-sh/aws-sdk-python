"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeregisterServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.service_id


class DeregisterServiceInput(TypedDict, closed=True):
    service_id: "capo_devops_agent.types.service_id.ServiceId"
    """<p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterServiceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterServiceInput:
    out: DeregisterServiceInput = {}  # type: ignore[typeddict-item]
    return out
