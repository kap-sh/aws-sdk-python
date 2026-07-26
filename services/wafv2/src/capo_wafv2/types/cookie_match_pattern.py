"""Generated from Smithy shape ``com.amazonaws.wafv2#CookieMatchPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.all
    import capo_wafv2.types.cookie_names


class CookieMatchPattern(TypedDict, closed=True):
    all: NotRequired["capo_wafv2.types.all.All"]
    """<p>Inspect all cookies. </p>"""
    included_cookies: NotRequired["capo_wafv2.types.cookie_names.CookieNames"]
    """<p>Inspect only the cookies that have a key that matches one of the strings specified here. </p>"""
    excluded_cookies: NotRequired["capo_wafv2.types.cookie_names.CookieNames"]
    """<p>Inspect only the cookies whose keys don't match any of the strings specified here. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CookieMatchPattern) -> dict:
    out: dict = {}
    if "all" in value:
        import capo_wafv2.types.all

        out["All"] = capo_wafv2.types.all.serialize_aws_json_1_1(value["all"])
    if "included_cookies" in value:
        import capo_wafv2.types.cookie_names

        out["IncludedCookies"] = capo_wafv2.types.cookie_names.serialize_aws_json_1_1(
            value["included_cookies"]
        )
    if "excluded_cookies" in value:
        import capo_wafv2.types.cookie_names

        out["ExcludedCookies"] = capo_wafv2.types.cookie_names.serialize_aws_json_1_1(
            value["excluded_cookies"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CookieMatchPattern:
    out: CookieMatchPattern = {}  # type: ignore[typeddict-item]
    if "All" in data:
        import capo_wafv2.types.all

        out["all"] = capo_wafv2.types.all.deserialize_aws_json_1_1(data["All"])
    if "IncludedCookies" in data:
        import capo_wafv2.types.cookie_names

        out["included_cookies"] = (
            capo_wafv2.types.cookie_names.deserialize_aws_json_1_1(
                data["IncludedCookies"]
            )
        )
    if "ExcludedCookies" in data:
        import capo_wafv2.types.cookie_names

        out["excluded_cookies"] = (
            capo_wafv2.types.cookie_names.deserialize_aws_json_1_1(
                data["ExcludedCookies"]
            )
        )
    return out
