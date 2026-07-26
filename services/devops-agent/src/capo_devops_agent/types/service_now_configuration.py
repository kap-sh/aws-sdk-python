"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceNowConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.service_now_authentication_scope_list


class ServiceNowConfiguration(TypedDict, closed=True):
    instance_id: NotRequired["str"]
    """<p>ServiceNow instance ID</p>"""
    auth_scopes: NotRequired[
        "capo_devops_agent.types.service_now_authentication_scope_list.ServiceNowAuthenticationScopeList"
    ]
    """<p>Scoped down authentication scopes for fine grained control</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowConfiguration) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "auth_scopes" in value:
        import capo_devops_agent.types.service_now_authentication_scope_list

        out["authScopes"] = (
            capo_devops_agent.types.service_now_authentication_scope_list.serialize_json(
                value["auth_scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceNowConfiguration:
    out: ServiceNowConfiguration = {}  # type: ignore[typeddict-item]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "authScopes" in data:
        import capo_devops_agent.types.service_now_authentication_scope_list

        out["auth_scopes"] = (
            capo_devops_agent.types.service_now_authentication_scope_list.deserialize_json(
                data["authScopes"]
            )
        )
    return out
