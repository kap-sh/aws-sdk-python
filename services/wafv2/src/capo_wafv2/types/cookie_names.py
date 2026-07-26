"""Generated from Smithy shape ``com.amazonaws.wafv2#CookieNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.single_cookie_name

CookieNames: TypeAlias = list["capo_wafv2.types.single_cookie_name.SingleCookieName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CookieNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CookieNames:
    return list(data)
