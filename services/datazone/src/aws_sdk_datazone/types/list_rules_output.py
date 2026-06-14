"""Generated from Smithy shape ``com.amazonaws.datazone#ListRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.rule_summaries


class ListRulesOutput(TypedDict):
    items: "aws_sdk_datazone.types.rule_summaries.RuleSummaries"
    """<p>The results of the <code>ListRules</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.rule_summaries

    out["items"] = aws_sdk_datazone.types.rule_summaries.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesOutput:
    out: ListRulesOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.rule_summaries

        out["items"] = aws_sdk_datazone.types.rule_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListRulesOutput.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
