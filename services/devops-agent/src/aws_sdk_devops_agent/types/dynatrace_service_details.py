"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceServiceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.dynatrace_service_authorization_config


class DynatraceServiceDetails(TypedDict):
    account_urn: "str"
    """<p>Dynatrace resource account urn.</p>"""
    authorization_config: NotRequired[
        "aws_sdk_devops_agent.types.dynatrace_service_authorization_config.DynatraceServiceAuthorizationConfig"
    ]
    """<p>Dynatrace OAuth client credentials configuration. Use this when registering with OAuth client credentials flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceServiceDetails) -> dict:
    out: dict = {}
    out["accountUrn"] = value["account_urn"]
    if "authorization_config" in value:
        import aws_sdk_devops_agent.types.dynatrace_service_authorization_config

        out["authorizationConfig"] = (
            aws_sdk_devops_agent.types.dynatrace_service_authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DynatraceServiceDetails:
    out: DynatraceServiceDetails = {}  # type: ignore[typeddict-item]
    if "accountUrn" in data:
        out["account_urn"] = data["accountUrn"]
    else:
        raise DeserializationError("DynatraceServiceDetails.account_urn required")
    if "authorizationConfig" in data:
        import aws_sdk_devops_agent.types.dynatrace_service_authorization_config

        out["authorization_config"] = (
            aws_sdk_devops_agent.types.dynatrace_service_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out
