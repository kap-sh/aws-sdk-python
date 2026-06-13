"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredServiceNowDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.service_now_instance_url


class RegisteredServiceNowDetails(TypedDict):
    instance_url: NotRequired[
        "aws_sdk_devops_agent.types.service_now_instance_url.ServiceNowInstanceUrl"
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
