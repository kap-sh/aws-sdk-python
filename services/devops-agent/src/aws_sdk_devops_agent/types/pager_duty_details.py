"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.pager_duty_authorization_config
    import aws_sdk_devops_agent.types.pager_duty_scopes


class PagerDutyDetails(TypedDict, closed=True):
    scopes: "aws_sdk_devops_agent.types.pager_duty_scopes.PagerDutyScopes"
    """<p>PagerDuty scopes.</p>"""
    authorization_config: "aws_sdk_devops_agent.types.pager_duty_authorization_config.PagerDutyAuthorizationConfig"
    """<p>PagerDuty authorization configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyDetails) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.pager_duty_scopes

    out["scopes"] = aws_sdk_devops_agent.types.pager_duty_scopes.serialize_json(
        value["scopes"]
    )
    import aws_sdk_devops_agent.types.pager_duty_authorization_config

    out["authorizationConfig"] = (
        aws_sdk_devops_agent.types.pager_duty_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PagerDutyDetails:
    out: PagerDutyDetails = {}  # type: ignore[typeddict-item]
    if "scopes" in data:
        import aws_sdk_devops_agent.types.pager_duty_scopes

        out["scopes"] = aws_sdk_devops_agent.types.pager_duty_scopes.deserialize_json(
            data["scopes"]
        )
    else:
        raise DeserializationError("PagerDutyDetails.scopes required")
    if "authorizationConfig" in data:
        import aws_sdk_devops_agent.types.pager_duty_authorization_config

        out["authorization_config"] = (
            aws_sdk_devops_agent.types.pager_duty_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError("PagerDutyDetails.authorization_config required")
    return out
