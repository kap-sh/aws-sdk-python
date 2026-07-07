"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.dynatrace_resource_list


class DynatraceConfiguration(TypedDict, closed=True):
    env_id: "str"
    """<p>Dynatrace environment id</p>"""
    resources: NotRequired[
        "aws_sdk_devops_agent.types.dynatrace_resource_list.DynatraceResourceList"
    ]
    """<p>List of Dynatrace resources to monitor</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceConfiguration) -> dict:
    out: dict = {}
    out["envId"] = value["env_id"]
    if "resources" in value:
        import aws_sdk_devops_agent.types.dynatrace_resource_list

        out["resources"] = (
            aws_sdk_devops_agent.types.dynatrace_resource_list.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> DynatraceConfiguration:
    out: DynatraceConfiguration = {}  # type: ignore[typeddict-item]
    if "envId" in data:
        out["env_id"] = data["envId"]
    else:
        raise DeserializationError("DynatraceConfiguration.env_id required")
    if "resources" in data:
        import aws_sdk_devops_agent.types.dynatrace_resource_list

        out["resources"] = (
            aws_sdk_devops_agent.types.dynatrace_resource_list.deserialize_json(
                data["resources"]
            )
        )
    return out
