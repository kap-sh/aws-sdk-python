"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_list_rules_output
    import capo_route53_recovery_readiness.types.__string


class ListRulesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    rules: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_list_rules_output.__listOfListRulesOutput"
    ]
    """<p>A list of readiness rules for a specific resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "rules" in value:
        import capo_route53_recovery_readiness.types.__list_of_list_rules_output

        out["rules"] = (
            capo_route53_recovery_readiness.types.__list_of_list_rules_output.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "rules" in data:
        import capo_route53_recovery_readiness.types.__list_of_list_rules_output

        out["rules"] = (
            capo_route53_recovery_readiness.types.__list_of_list_rules_output.deserialize_json(
                data["rules"]
            )
        )
    return out
