"""Generated from Smithy shape ``com.amazonaws.lightsail#CacheBehavior``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.behavior_enum


class CacheBehavior(TypedDict):
    behavior: NotRequired["aws_sdk_lightsail.types.behavior_enum.BehaviorEnum"]
    """<p>The cache behavior of the distribution.</p> <p>The following cache behaviors can be specified:</p> <ul> <li> <p> <b> <code>cache</code> </b> - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesn't change depending on who views it, or for websites that don't use cookies, headers, or query strings to personalize content.</p> </li> <li> <p> <b> <code>dont-cache</code> </b> - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serve only the content that is specified in the distribution's <code>CacheBehaviorPerPath</code> parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheBehavior) -> dict:
    out: dict = {}
    if "behavior" in value:
        import aws_sdk_lightsail.types.behavior_enum

        out["behavior"] = aws_sdk_lightsail.types.behavior_enum.serialize_aws_json_1_1(
            value["behavior"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheBehavior:
    out: CacheBehavior = {}  # type: ignore[typeddict-item]
    if "behavior" in data:
        import aws_sdk_lightsail.types.behavior_enum

        out["behavior"] = (
            aws_sdk_lightsail.types.behavior_enum.deserialize_aws_json_1_1(
                data["behavior"]
            )
        )
    return out
