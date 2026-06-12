"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchSetUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.byte_match_tuple
    import aws_sdk_waf.types.change_action


class ByteMatchSetUpdate(TypedDict):
    action: "aws_sdk_waf.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a <a>ByteMatchTuple</a>.</p>"""
    byte_match_tuple: "aws_sdk_waf.types.byte_match_tuple.ByteMatchTuple"
    """<p>Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify <code>DELETE</code> for the value of <code>Action</code>, the <code>ByteMatchTuple</code> values must exactly match the values in the <code>ByteMatchTuple</code> that you want to delete from the <code>ByteMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSetUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf.types.change_action

    out["Action"] = aws_sdk_waf.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import aws_sdk_waf.types.byte_match_tuple

    out["ByteMatchTuple"] = aws_sdk_waf.types.byte_match_tuple.serialize_aws_json_1_1(
        value["byte_match_tuple"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByteMatchSetUpdate:
    out: ByteMatchSetUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf.types.change_action

        out["action"] = aws_sdk_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("ByteMatchSetUpdate.action required")
    if "ByteMatchTuple" in data:
        import aws_sdk_waf.types.byte_match_tuple

        out["byte_match_tuple"] = (
            aws_sdk_waf.types.byte_match_tuple.deserialize_aws_json_1_1(
                data["ByteMatchTuple"]
            )
        )
    else:
        raise DeserializationError("ByteMatchSetUpdate.byte_match_tuple required")
    return out
