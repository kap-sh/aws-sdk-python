"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthorizationRuleStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_authorization_rule_status_code
    import capo_ec2.types.string


class ClientVpnAuthorizationRuleStatus(TypedDict, closed=True):
    code: NotRequired[
        "capo_ec2.types.client_vpn_authorization_rule_status_code.ClientVpnAuthorizationRuleStatusCode"
    ]
    """<p>The state of the authorization rule.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message about the status of the authorization rule, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnAuthorizationRuleStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_ec2.types.client_vpn_authorization_rule_status_code

        capo_ec2.types.client_vpn_authorization_rule_status_code.serialize_ec2_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> ClientVpnAuthorizationRuleStatus:
    out: ClientVpnAuthorizationRuleStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        import capo_ec2.types.client_vpn_authorization_rule_status_code

        out["code"] = (
            capo_ec2.types.client_vpn_authorization_rule_status_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
