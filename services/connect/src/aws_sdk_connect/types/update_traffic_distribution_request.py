"""Generated from Smithy shape ``com.amazonaws.connect#UpdateTrafficDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_config
    import aws_sdk_connect.types.sign_in_config
    import aws_sdk_connect.types.telephony_config
    import aws_sdk_connect.types.traffic_distribution_group_id_or_arn


class UpdateTrafficDistributionRequest(TypedDict):
    id: "aws_sdk_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region. </p>"""
    telephony_config: NotRequired[
        "aws_sdk_connect.types.telephony_config.TelephonyConfig"
    ]
    """<p>The distribution of traffic between the instance and its replica(s).</p>"""
    sign_in_config: NotRequired["aws_sdk_connect.types.sign_in_config.SignInConfig"]
    """<p>The distribution that determines which Amazon Web Services Regions should be used to sign in agents in to both the instance and its replica(s).</p>"""
    agent_config: NotRequired["aws_sdk_connect.types.agent_config.AgentConfig"]
    """<p>The distribution of agents between the instance and its replica(s).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrafficDistributionRequest) -> dict:
    out: dict = {}
    if "telephony_config" in value:
        import aws_sdk_connect.types.telephony_config

        out["TelephonyConfig"] = aws_sdk_connect.types.telephony_config.serialize_json(
            value["telephony_config"]
        )
    if "sign_in_config" in value:
        import aws_sdk_connect.types.sign_in_config

        out["SignInConfig"] = aws_sdk_connect.types.sign_in_config.serialize_json(
            value["sign_in_config"]
        )
    if "agent_config" in value:
        import aws_sdk_connect.types.agent_config

        out["AgentConfig"] = aws_sdk_connect.types.agent_config.serialize_json(
            value["agent_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTrafficDistributionRequest:
    out: UpdateTrafficDistributionRequest = {}  # type: ignore[typeddict-item]
    if "TelephonyConfig" in data:
        import aws_sdk_connect.types.telephony_config

        out["telephony_config"] = (
            aws_sdk_connect.types.telephony_config.deserialize_json(
                data["TelephonyConfig"]
            )
        )
    if "SignInConfig" in data:
        import aws_sdk_connect.types.sign_in_config

        out["sign_in_config"] = aws_sdk_connect.types.sign_in_config.deserialize_json(
            data["SignInConfig"]
        )
    if "AgentConfig" in data:
        import aws_sdk_connect.types.agent_config

        out["agent_config"] = aws_sdk_connect.types.agent_config.deserialize_json(
            data["AgentConfig"]
        )
    return out
