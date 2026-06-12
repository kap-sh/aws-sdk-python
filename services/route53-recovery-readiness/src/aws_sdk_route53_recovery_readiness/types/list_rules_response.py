"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output
    import aws_sdk_route53_recovery_readiness.types.__string


class ListRulesResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    rules: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output.__listOfListRulesOutput"
    ]
    """<p>A list of readiness rules for a specific resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "rules" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output

        out["rules"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "rules" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output

        out["rules"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_list_rules_output.deserialize_json(
                data["rules"]
            )
        )
    return out
