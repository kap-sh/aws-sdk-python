"""Generated from Smithy shape ``com.amazonaws.wafv2#AWSManagedRulesAntiDDoSRuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.client_side_action_config
    import capo_wafv2.types.sensitivity_to_act


class AWSManagedRulesAntiDDoSRuleSet(TypedDict, closed=True):
    client_side_action_config: (
        "capo_wafv2.types.client_side_action_config.ClientSideActionConfig"
    )
    """<p>Configures the request handling that's applied by the managed rule group rules <code>ChallengeAllDuringEvent</code> and <code>ChallengeDDoSRequests</code> during a distributed denial of service (DDoS) attack.</p>"""
    sensitivity_to_block: NotRequired[
        "capo_wafv2.types.sensitivity_to_act.SensitivityToAct"
    ]
    """<p>The sensitivity that the rule group rule <code>DDoSRequests</code> uses when matching against the DDoS suspicion labeling on a request. The managed rule group adds the labeling during DDoS events, before the <code>DDoSRequests</code> rule runs. </p> <p>The higher the sensitivity, the more levels of labeling that the rule matches: </p> <ul> <li> <p>Low sensitivity is less sensitive, causing the rule to match only on the most likely participants in an attack, which are the requests with the high suspicion label <code>awswaf:managed:aws:anti-ddos:high-suspicion-ddos-request</code>.</p> </li> <li> <p>Medium sensitivity causes the rule to match on the medium and high suspicion labels.</p> </li> <li> <p>High sensitivity causes the rule to match on all of the suspicion labels: low, medium, and high.</p> </li> </ul> <p>Default: <code>LOW</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSManagedRulesAntiDDoSRuleSet) -> dict:
    out: dict = {}
    import capo_wafv2.types.client_side_action_config

    out["ClientSideActionConfig"] = (
        capo_wafv2.types.client_side_action_config.serialize_aws_json_1_1(
            value["client_side_action_config"]
        )
    )
    if "sensitivity_to_block" in value:
        import capo_wafv2.types.sensitivity_to_act

        out["SensitivityToBlock"] = (
            capo_wafv2.types.sensitivity_to_act.serialize_aws_json_1_1(
                value["sensitivity_to_block"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSManagedRulesAntiDDoSRuleSet:
    out: AWSManagedRulesAntiDDoSRuleSet = {}  # type: ignore[typeddict-item]
    if "ClientSideActionConfig" in data:
        import capo_wafv2.types.client_side_action_config

        out["client_side_action_config"] = (
            capo_wafv2.types.client_side_action_config.deserialize_aws_json_1_1(
                data["ClientSideActionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AWSManagedRulesAntiDDoSRuleSet.client_side_action_config required"
        )
    if "SensitivityToBlock" in data:
        import capo_wafv2.types.sensitivity_to_act

        out["sensitivity_to_block"] = (
            capo_wafv2.types.sensitivity_to_act.deserialize_aws_json_1_1(
                data["SensitivityToBlock"]
            )
        )
    return out
