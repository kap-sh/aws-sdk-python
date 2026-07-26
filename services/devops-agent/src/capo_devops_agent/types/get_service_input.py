"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.service_id


class GetServiceInput(TypedDict, closed=True):
    service_id: "capo_devops_agent.types.service_id.ServiceId"
    """<p>The unique identifier of the given service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceInput:
    out: GetServiceInput = {}  # type: ignore[typeddict-item]
    return out
