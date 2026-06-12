"""Generated from Smithy shape ``com.amazonaws.lightsail#CookieObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.forward_values
    import aws_sdk_lightsail.types.string_list


class CookieObject(TypedDict):
    option: NotRequired["aws_sdk_lightsail.types.forward_values.ForwardValues"]
    """<p>Specifies which cookies to forward to the distribution's origin for a cache behavior: <code>all</code>, <code>none</code>, or <code>allow-list</code> to forward only the cookies specified in the <code>cookiesAllowList</code> parameter.</p>"""
    cookies_allow_list: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>The specific cookies to forward to your distribution's origin.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CookieObject) -> dict:
    out: dict = {}
    if "option" in value:
        import aws_sdk_lightsail.types.forward_values

        out["option"] = aws_sdk_lightsail.types.forward_values.serialize_aws_json_1_1(
            value["option"]
        )
    if "cookies_allow_list" in value:
        import aws_sdk_lightsail.types.string_list

        out["cookiesAllowList"] = (
            aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
                value["cookies_allow_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CookieObject:
    out: CookieObject = {}  # type: ignore[typeddict-item]
    if "option" in data:
        import aws_sdk_lightsail.types.forward_values

        out["option"] = aws_sdk_lightsail.types.forward_values.deserialize_aws_json_1_1(
            data["option"]
        )
    if "cookiesAllowList" in data:
        import aws_sdk_lightsail.types.string_list

        out["cookies_allow_list"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["cookiesAllowList"]
            )
        )
    return out
