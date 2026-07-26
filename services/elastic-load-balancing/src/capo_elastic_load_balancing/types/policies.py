"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Policies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policies
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policies
    import capo_elastic_load_balancing.types.policy_names


class Policies(TypedDict, closed=True):
    app_cookie_stickiness_policies: NotRequired[
        "capo_elastic_load_balancing.types.app_cookie_stickiness_policies.AppCookieStickinessPolicies"
    ]
    """<p>The stickiness policies created using <a>CreateAppCookieStickinessPolicy</a>.</p>"""
    lb_cookie_stickiness_policies: NotRequired[
        "capo_elastic_load_balancing.types.lb_cookie_stickiness_policies.LBCookieStickinessPolicies"
    ]
    """<p>The stickiness policies created using <a>CreateLBCookieStickinessPolicy</a>.</p>"""
    other_policies: NotRequired[
        "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    ]
    """<p>The policies other than the stickiness policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Policies, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "app_cookie_stickiness_policies" in value:
        import capo_elastic_load_balancing.types.app_cookie_stickiness_policies

        capo_elastic_load_balancing.types.app_cookie_stickiness_policies.serialize_query(
            value["app_cookie_stickiness_policies"],
            pairs,
            f"{prefix}.AppCookieStickinessPolicies",
        )
    if "lb_cookie_stickiness_policies" in value:
        import capo_elastic_load_balancing.types.lb_cookie_stickiness_policies

        capo_elastic_load_balancing.types.lb_cookie_stickiness_policies.serialize_query(
            value["lb_cookie_stickiness_policies"],
            pairs,
            f"{prefix}.LBCookieStickinessPolicies",
        )
    if "other_policies" in value:
        import capo_elastic_load_balancing.types.policy_names

        capo_elastic_load_balancing.types.policy_names.serialize_query(
            value["other_policies"], pairs, f"{prefix}.OtherPolicies"
        )


def deserialize_query(el: Element) -> Policies:
    out: Policies = {}  # type: ignore[typeddict-item]
    child_app_cookie_stickiness_policies = el.find("AppCookieStickinessPolicies")
    if child_app_cookie_stickiness_policies is not None:
        import capo_elastic_load_balancing.types.app_cookie_stickiness_policies

        out["app_cookie_stickiness_policies"] = (
            capo_elastic_load_balancing.types.app_cookie_stickiness_policies.deserialize_query(
                child_app_cookie_stickiness_policies
            )
        )
    child_lb_cookie_stickiness_policies = el.find("LBCookieStickinessPolicies")
    if child_lb_cookie_stickiness_policies is not None:
        import capo_elastic_load_balancing.types.lb_cookie_stickiness_policies

        out["lb_cookie_stickiness_policies"] = (
            capo_elastic_load_balancing.types.lb_cookie_stickiness_policies.deserialize_query(
                child_lb_cookie_stickiness_policies
            )
        )
    child_other_policies = el.find("OtherPolicies")
    if child_other_policies is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["other_policies"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_other_policies
            )
        )
    return out
