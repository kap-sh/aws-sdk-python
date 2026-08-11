"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AppCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policy

AppCookieStickinessPolicies: TypeAlias = list[
    "capo_elastic_load_balancing.types.app_cookie_stickiness_policy.AppCookieStickinessPolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AppCookieStickinessPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policy

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.app_cookie_stickiness_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AppCookieStickinessPolicies:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policy

    out: AppCookieStickinessPolicies = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.app_cookie_stickiness_policy.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AppCookieStickinessPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policy

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.app_cookie_stickiness_policy.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AppCookieStickinessPolicies:
    import capo_elastic_load_balancing.types.app_cookie_stickiness_policy

    out: AppCookieStickinessPolicies = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.app_cookie_stickiness_policy.deserialize_query(
                child
            )
        )
    return out
