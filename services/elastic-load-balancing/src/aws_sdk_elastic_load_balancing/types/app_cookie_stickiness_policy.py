"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AppCookieStickinessPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.cookie_name
    import aws_sdk_elastic_load_balancing.types.policy_name


class AppCookieStickinessPolicy(TypedDict):
    policy_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_name.PolicyName"
    ]
    """<p>The mnemonic name for the policy being created. The name must be unique within a set of policies for this load balancer.</p>"""
    cookie_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.cookie_name.CookieName"
    ]
    """<p>The name of the application cookie used for stickiness.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AppCookieStickinessPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "cookie_name" in value:
        pairs.append((f"{prefix}.CookieName", str(value["cookie_name"])))


def deserialize_query(el: Element) -> AppCookieStickinessPolicy:
    out: AppCookieStickinessPolicy = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_cookie_name = el.find("CookieName")
    if child_cookie_name is not None:
        out["cookie_name"] = str(child_cookie_name.text or "")
    return out
