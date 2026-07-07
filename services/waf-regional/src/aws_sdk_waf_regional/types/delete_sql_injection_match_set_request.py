"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.resource_id


class DeleteSqlInjectionMatchSetRequest(TypedDict, closed=True):
    sql_injection_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to delete. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSqlInjectionMatchSetRequest:
    out: DeleteSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "SqlInjectionMatchSetId" in data:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        raise DeserializationError(
            "DeleteSqlInjectionMatchSetRequest.sql_injection_match_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError(
            "DeleteSqlInjectionMatchSetRequest.change_token required"
        )
    return out
