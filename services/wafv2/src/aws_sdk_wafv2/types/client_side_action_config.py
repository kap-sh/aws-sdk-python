"""Generated from Smithy shape ``com.amazonaws.wafv2#ClientSideActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.client_side_action


class ClientSideActionConfig(TypedDict, closed=True):
    challenge: "aws_sdk_wafv2.types.client_side_action.ClientSideAction"
    """<p>Configuration for the use of the <code>AWSManagedRulesAntiDDoSRuleSet</code> rules <code>ChallengeAllDuringEvent</code> and <code>ChallengeDDoSRequests</code>. </p> <note> <p>This setting isn't related to the configuration of the <code>Challenge</code> action itself. It only configures the use of the two anti-DDoS rules named here. </p> </note> <p>You can enable or disable the use of these rules, and you can configure how to use them when they are enabled. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSideActionConfig) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.client_side_action

    out["Challenge"] = aws_sdk_wafv2.types.client_side_action.serialize_aws_json_1_1(
        value["challenge"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientSideActionConfig:
    out: ClientSideActionConfig = {}  # type: ignore[typeddict-item]
    if "Challenge" in data:
        import aws_sdk_wafv2.types.client_side_action

        out["challenge"] = (
            aws_sdk_wafv2.types.client_side_action.deserialize_aws_json_1_1(
                data["Challenge"]
            )
        )
    else:
        raise DeserializationError("ClientSideActionConfig.challenge required")
    return out
