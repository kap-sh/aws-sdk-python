"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListRuleSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.rule_sets


class ListRuleSetsResponse(TypedDict, closed=True):
    rule_sets: "aws_sdk_mailmanager.types.rule_sets.RuleSets"
    """<p>The list of rule sets.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleSetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.rule_sets

    out["RuleSets"] = aws_sdk_mailmanager.types.rule_sets.serialize_aws_json_1_0(
        value["rule_sets"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleSetsResponse:
    out: ListRuleSetsResponse = {}  # type: ignore[typeddict-item]
    if "RuleSets" in data:
        import aws_sdk_mailmanager.types.rule_sets

        out["rule_sets"] = aws_sdk_mailmanager.types.rule_sets.deserialize_aws_json_1_0(
            data["RuleSets"]
        )
    else:
        raise DeserializationError("ListRuleSetsResponse.rule_sets required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
