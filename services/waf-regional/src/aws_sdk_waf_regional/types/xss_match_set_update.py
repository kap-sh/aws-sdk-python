"""Generated from Smithy shape ``com.amazonaws.wafregional#XssMatchSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_action
    import aws_sdk_waf_regional.types.xss_match_tuple


class XssMatchSetUpdate(TypedDict, closed=True):
    action: "aws_sdk_waf_regional.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add an <a>XssMatchSetUpdate</a> to an <a>XssMatchSet</a>. Use <code>DELETE</code> to remove an <code>XssMatchSetUpdate</code> from an <code>XssMatchSet</code>.</p>"""
    xss_match_tuple: "aws_sdk_waf_regional.types.xss_match_tuple.XssMatchTuple"
    """<p>Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSetUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf_regional.types.change_action

    out["Action"] = aws_sdk_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import aws_sdk_waf_regional.types.xss_match_tuple

    out["XssMatchTuple"] = (
        aws_sdk_waf_regional.types.xss_match_tuple.serialize_aws_json_1_1(
            value["xss_match_tuple"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> XssMatchSetUpdate:
    out: XssMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf_regional.types.change_action

        out["action"] = (
            aws_sdk_waf_regional.types.change_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("XssMatchSetUpdate.action required")
    if "XssMatchTuple" in data:
        import aws_sdk_waf_regional.types.xss_match_tuple

        out["xss_match_tuple"] = (
            aws_sdk_waf_regional.types.xss_match_tuple.deserialize_aws_json_1_1(
                data["XssMatchTuple"]
            )
        )
    else:
        raise DeserializationError("XssMatchSetUpdate.xss_match_tuple required")
    return out
