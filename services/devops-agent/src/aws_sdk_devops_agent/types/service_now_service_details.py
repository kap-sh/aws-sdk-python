"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceNowServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.service_now_instance_url
    import aws_sdk_devops_agent.types.service_now_service_authorization_config


class ServiceNowServiceDetails(TypedDict, closed=True):
    instance_url: (
        "aws_sdk_devops_agent.types.service_now_instance_url.ServiceNowInstanceUrl"
    )
    """<p>ServiceNow instance URL.</p>"""
    authorization_config: NotRequired[
        "aws_sdk_devops_agent.types.service_now_service_authorization_config.ServiceNowServiceAuthorizationConfig"
    ]
    """<p>ServiceNow OAuth client credentials configuration. Use this when registering with OAuth client credentials flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowServiceDetails) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    if "authorization_config" in value:
        import aws_sdk_devops_agent.types.service_now_service_authorization_config

        out["authorizationConfig"] = (
            aws_sdk_devops_agent.types.service_now_service_authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceNowServiceDetails:
    out: ServiceNowServiceDetails = {}  # type: ignore[typeddict-item]
    if "instanceUrl" in data:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError("ServiceNowServiceDetails.instance_url required")
    if "authorizationConfig" in data:
        import aws_sdk_devops_agent.types.service_now_service_authorization_config

        out["authorization_config"] = (
            aws_sdk_devops_agent.types.service_now_service_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out
