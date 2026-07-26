"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.self_managed_input
    import capo_devops_agent.types.service_managed_input


class _PrivateConnectionMode_serviceManaged(TypedDict, closed=True):
    serviceManaged: "capo_devops_agent.types.service_managed_input.ServiceManagedInput"


class _PrivateConnectionMode_selfManaged(TypedDict, closed=True):
    selfManaged: "capo_devops_agent.types.self_managed_input.SelfManagedInput"


PrivateConnectionMode: TypeAlias = (
    _PrivateConnectionMode_serviceManaged | _PrivateConnectionMode_selfManaged
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionMode) -> dict:
    if "serviceManaged" in value:
        import capo_devops_agent.types.service_managed_input

        return {
            "serviceManaged": capo_devops_agent.types.service_managed_input.serialize_json(
                value["serviceManaged"]
            )
        }
    elif "selfManaged" in value:
        import capo_devops_agent.types.self_managed_input

        return {
            "selfManaged": capo_devops_agent.types.self_managed_input.serialize_json(
                value["selfManaged"]
            )
        }
    else:
        raise SerializationError("PrivateConnectionMode: no variant present")


def deserialize_json(data: dict) -> PrivateConnectionMode:
    if "serviceManaged" in data:
        import capo_devops_agent.types.service_managed_input

        return {
            "serviceManaged": capo_devops_agent.types.service_managed_input.deserialize_json(
                data["serviceManaged"]
            )
        }
    elif "selfManaged" in data:
        import capo_devops_agent.types.self_managed_input

        return {
            "selfManaged": capo_devops_agent.types.self_managed_input.deserialize_json(
                data["selfManaged"]
            )
        }
    else:
        raise DeserializationError("PrivateConnectionMode: no recognized variant key")
