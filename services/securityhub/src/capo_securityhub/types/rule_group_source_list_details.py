"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class RuleGroupSourceListDetails(TypedDict, closed=True):
    generated_rules_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether to allow or deny access to the domains listed in <code>Targets</code>.</p>"""
    target_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The protocols that you want to inspect. Specify <code>LS_SNI</code> for HTTPS. Specify <code>HTTP_HOST</code> for HTTP. You can specify either or both.</p>"""
    targets: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The domains that you want to inspect for in your traffic flows. You can provide full domain names, or use the '.' prefix as a wildcard. For example, <code>.example.com</code> matches all domains that end with <code>example.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceListDetails) -> dict:
    out: dict = {}
    if "generated_rules_type" in value:
        out["GeneratedRulesType"] = value["generated_rules_type"]
    if "target_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["TargetTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["target_types"]
            )
        )
    if "targets" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Targets"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["targets"]
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceListDetails:
    out: RuleGroupSourceListDetails = {}  # type: ignore[typeddict-item]
    if "GeneratedRulesType" in data:
        out["generated_rules_type"] = data["GeneratedRulesType"]
    if "TargetTypes" in data:
        import capo_securityhub.types.non_empty_string_list

        out["target_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["TargetTypes"]
            )
        )
    if "Targets" in data:
        import capo_securityhub.types.non_empty_string_list

        out["targets"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Targets"]
        )
    return out
