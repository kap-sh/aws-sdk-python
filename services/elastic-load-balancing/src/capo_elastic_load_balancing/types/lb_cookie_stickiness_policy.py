"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LBCookieStickinessPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.cookie_expiration_period
    import capo_elastic_load_balancing.types.policy_name


class LBCookieStickinessPolicy(TypedDict, closed=True):
    policy_name: NotRequired["capo_elastic_load_balancing.types.policy_name.PolicyName"]
    """<p>The name of the policy. This name must be unique within the set of policies for this load balancer.</p>"""
    cookie_expiration_period: NotRequired[
        "capo_elastic_load_balancing.types.cookie_expiration_period.CookieExpirationPeriod"
    ]
    """<p>The time period, in seconds, after which the cookie should be considered stale. If this parameter is not specified, the stickiness session lasts for the duration of the browser session.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LBCookieStickinessPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "cookie_expiration_period" in value:
        pairs.append(
            (f"{prefix}.CookieExpirationPeriod", str(value["cookie_expiration_period"]))
        )


def deserialize_query(el: Element) -> LBCookieStickinessPolicy:
    out: LBCookieStickinessPolicy = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_cookie_expiration_period = el.find("CookieExpirationPeriod")
    if child_cookie_expiration_period is not None:
        out["cookie_expiration_period"] = int(child_cookie_expiration_period.text or "")
    return out
