"""Generated from Smithy shape ``com.amazonaws.waf#UpdateSqlInjectionMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_id
    import aws_sdk_waf.types.sql_injection_match_set_updates


class UpdateSqlInjectionMatchSetRequest(TypedDict):
    sql_injection_match_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>SqlInjectionMatchSetId</code> of the <code>SqlInjectionMatchSet</code> that you want to update. <code>SqlInjectionMatchSetId</code> is returned by <a>CreateSqlInjectionMatchSet</a> and by <a>ListSqlInjectionMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: (
        "aws_sdk_waf.types.sql_injection_match_set_updates.SqlInjectionMatchSetUpdates"
    )
    """<p>An array of <code>SqlInjectionMatchSetUpdate</code> objects that you want to insert into or delete from a <a>SqlInjectionMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>SqlInjectionMatchSetUpdate</a>: Contains <code>Action</code> and <code>SqlInjectionMatchTuple</code> </p> </li> <li> <p> <a>SqlInjectionMatchTuple</a>: Contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSqlInjectionMatchSetRequest) -> dict:
    out: dict = {}
    out["SqlInjectionMatchSetId"] = value["sql_injection_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import aws_sdk_waf.types.sql_injection_match_set_updates

    out["Updates"] = (
        aws_sdk_waf.types.sql_injection_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSqlInjectionMatchSetRequest:
    out: UpdateSqlInjectionMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "SqlInjectionMatchSetId" in data:
        out["sql_injection_match_set_id"] = data["SqlInjectionMatchSetId"]
    else:
        raise DeserializationError(
            "UpdateSqlInjectionMatchSetRequest.sql_injection_match_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError(
            "UpdateSqlInjectionMatchSetRequest.change_token required"
        )
    if "Updates" in data:
        import aws_sdk_waf.types.sql_injection_match_set_updates

        out["updates"] = (
            aws_sdk_waf.types.sql_injection_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateSqlInjectionMatchSetRequest.updates required")
    return out
