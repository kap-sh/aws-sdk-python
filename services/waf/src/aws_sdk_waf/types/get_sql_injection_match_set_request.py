"""Generated from Smithy shape ``com.amazonaws.waf#GetSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.resource_id


class GetSqlInjectionMatchSetRequest(TypedDict):
    sql_injection_match_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <a>SqlInjectionMatchSet</a> that you want to get. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSqlInjectionMatchSetRequest:
    out: GetSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "SqlInjectionMatchSetId" in data:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        raise DeserializationError(
            "GetSqlInjectionMatchSetRequest.sql_injection_match_set_id required"
        )
    return out
