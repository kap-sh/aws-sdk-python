"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredServiceNowDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.service_now_instance_url


class RegisteredServiceNowDetails(TypedDict, closed=True):
    instance_url: NotRequired[
        "capo_devops_agent.types.service_now_instance_url.ServiceNowInstanceUrl"
    ]
    """<p>The ServiceNow instance url</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredServiceNowDetails) -> dict:
    out: dict = {}
    if "instance_url" in value:
        out["instanceUrl"] = value["instance_url"]
    return out


def deserialize_json(data: dict) -> RegisteredServiceNowDetails:
    out: RegisteredServiceNowDetails = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    return out
