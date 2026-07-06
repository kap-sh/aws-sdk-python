"""Generated from Smithy shape ``com.amazonaws.wafv2#JA4Fingerprint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.fallback_behavior


class JA4Fingerprint(TypedDict, closed=True):
    fallback_behavior: "aws_sdk_wafv2.types.fallback_behavior.FallbackBehavior"
    """<p>The match status to assign to the web request if the request doesn't have a JA4 fingerprint. </p> <p>You can specify the following fallback behaviors:</p> <ul> <li> <p> <code>MATCH</code> - Treat the web request as matching the rule statement. WAF applies the rule action to the request.</p> </li> <li> <p> <code>NO_MATCH</code> - Treat the web request as not matching the rule statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JA4Fingerprint) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.fallback_behavior

    out["FallbackBehavior"] = (
        aws_sdk_wafv2.types.fallback_behavior.serialize_aws_json_1_1(
            value["fallback_behavior"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> JA4Fingerprint:
    out: JA4Fingerprint = {}  # type: ignore[typeddict-item]
    if "FallbackBehavior" in data:
        import aws_sdk_wafv2.types.fallback_behavior

        out["fallback_behavior"] = (
            aws_sdk_wafv2.types.fallback_behavior.deserialize_aws_json_1_1(
                data["FallbackBehavior"]
            )
        )
    else:
        raise DeserializationError("JA4Fingerprint.fallback_behavior required")
    return out
