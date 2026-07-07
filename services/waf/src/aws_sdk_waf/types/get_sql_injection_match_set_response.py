"""Generated from Smithy shape ``com.amazonaws.waf#GetSqlInjectionMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.sql_injection_match_set


class GetSqlInjectionMatchSetResponse(TypedDict, closed=True):
    sql_injection_match_set: NotRequired[
        "aws_sdk_waf.types.sql_injection_match_set.SqlInjectionMatchSet"
    ]
    """<p>Information about the <a>SqlInjectionMatchSet</a> that you specified in the <code>GetSqlInjectionMatchSet</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>SqlInjectionMatchSet</a>: Contains <code>Name</code>, <code>SqlInjectionMatchSetId</code>, and an array of <code>SqlInjectionMatchTuple</code> objects</p> </li> <li> <p> <a>SqlInjectionMatchTuple</a>: Each <code>SqlInjectionMatchTuple</code> object contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSqlInjectionMatchSetResponse) -> dict:
    out: dict = {}
    if "sql_injection_match_set" in value:
        import aws_sdk_waf.types.sql_injection_match_set

        out["SqlInjectionMatchSet"] = (
            aws_sdk_waf.types.sql_injection_match_set.serialize_aws_json_1_1(
                value["sql_injection_match_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSqlInjectionMatchSetResponse:
    out: GetSqlInjectionMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "SqlInjectionMatchSet" in data:
        import aws_sdk_waf.types.sql_injection_match_set

        out["sql_injection_match_set"] = (
            aws_sdk_waf.types.sql_injection_match_set.deserialize_aws_json_1_1(
                data["SqlInjectionMatchSet"]
            )
        )
    return out
