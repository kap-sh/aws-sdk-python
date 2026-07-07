"""Generated from Smithy shape ``com.amazonaws.waf#ListSqlInjectionMatchSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.next_marker
    import aws_sdk_waf.types.sql_injection_match_set_summaries


class ListSqlInjectionMatchSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>If you have more <a>SqlInjectionMatchSet</a> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>SqlInjectionMatchSet</code> objects, submit another <code>ListSqlInjectionMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    sql_injection_match_sets: NotRequired[
        "aws_sdk_waf.types.sql_injection_match_set_summaries.SqlInjectionMatchSetSummaries"
    ]
    """<p>An array of <a>SqlInjectionMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSqlInjectionMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "sql_injection_match_sets" in value:
        import aws_sdk_waf.types.sql_injection_match_set_summaries

        out["SqlInjectionMatchSets"] = (
            aws_sdk_waf.types.sql_injection_match_set_summaries.serialize_aws_json_1_1(
                value["sql_injection_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSqlInjectionMatchSetsResponse:
    out: ListSqlInjectionMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "SqlInjectionMatchSets" in data:
        import aws_sdk_waf.types.sql_injection_match_set_summaries

        out["sql_injection_match_sets"] = (
            aws_sdk_waf.types.sql_injection_match_set_summaries.deserialize_aws_json_1_1(
                data["SqlInjectionMatchSets"]
            )
        )
    return out
