"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.registered_services_list


class ListServicesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    services: (
        "aws_sdk_devops_agent.types.registered_services_list.RegisteredServicesList"
    )


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_devops_agent.types.registered_services_list

    out["services"] = (
        aws_sdk_devops_agent.types.registered_services_list.serialize_json(
            value["services"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "services" in data:
        import aws_sdk_devops_agent.types.registered_services_list

        out["services"] = (
            aws_sdk_devops_agent.types.registered_services_list.deserialize_json(
                data["services"]
            )
        )
    else:
        raise DeserializationError("ListServicesOutput.services required")
    return out
