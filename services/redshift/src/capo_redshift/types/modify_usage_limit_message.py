"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyUsageLimitMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.long_optional
    import capo_redshift.types.string
    import capo_redshift.types.usage_limit_breach_action


class ModifyUsageLimitMessage(TypedDict, closed=True):
    usage_limit_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the usage limit to modify.</p>"""
    amount: NotRequired["capo_redshift.types.long_optional.LongOptional"]
    """<p>The new limit amount. For more information about this parameter, see <a>UsageLimit</a>. </p>"""
    breach_action: NotRequired[
        "capo_redshift.types.usage_limit_breach_action.UsageLimitBreachAction"
    ]
    """<p>The new action that Amazon Redshift takes when the limit is reached. For more information about this parameter, see <a>UsageLimit</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyUsageLimitMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "usage_limit_id" in value:
        pairs.append((f"{key_prefix}UsageLimitId", str(value["usage_limit_id"])))
    if "amount" in value:
        pairs.append((f"{key_prefix}Amount", str(value["amount"])))
    if "breach_action" in value:
        import capo_redshift.types.usage_limit_breach_action

        capo_redshift.types.usage_limit_breach_action.serialize_query(
            value["breach_action"], pairs, f"{key_prefix}BreachAction"
        )


def deserialize_query(el: Element) -> ModifyUsageLimitMessage:
    out: ModifyUsageLimitMessage = {}  # type: ignore[typeddict-item]
    child_usage_limit_id = el.find("UsageLimitId")
    if child_usage_limit_id is not None:
        out["usage_limit_id"] = str(child_usage_limit_id.text or "")
    child_amount = el.find("Amount")
    if child_amount is not None:
        out["amount"] = int(child_amount.text or "")
    child_breach_action = el.find("BreachAction")
    if child_breach_action is not None:
        import capo_redshift.types.usage_limit_breach_action

        out["breach_action"] = (
            capo_redshift.types.usage_limit_breach_action.deserialize_query(
                child_breach_action
            )
        )
    return out
