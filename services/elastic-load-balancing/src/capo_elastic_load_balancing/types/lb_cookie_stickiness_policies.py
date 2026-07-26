"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#LBCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policy

LBCookieStickinessPolicies: TypeAlias = list[
    "capo_elastic_load_balancing.types.lb_cookie_stickiness_policy.LBCookieStickinessPolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: LBCookieStickinessPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policy

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.lb_cookie_stickiness_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> LBCookieStickinessPolicies:
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policy

    out: LBCookieStickinessPolicies = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.lb_cookie_stickiness_policy.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: LBCookieStickinessPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policy

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.lb_cookie_stickiness_policy.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> LBCookieStickinessPolicies:
    import capo_elastic_load_balancing.types.lb_cookie_stickiness_policy

    out: LBCookieStickinessPolicies = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.lb_cookie_stickiness_policy.deserialize_query(
                child
            )
        )
    return out
