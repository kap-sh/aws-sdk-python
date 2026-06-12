"""Generated from Smithy shape ``com.amazonaws.databrew#ListRulesetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.next_token
    import aws_sdk_databrew.types.ruleset_item_list


class ListRulesetsResponse(TypedDict):
    rulesets: "aws_sdk_databrew.types.ruleset_item_list.RulesetItemList"
    """<p>A list of RulesetItem. RulesetItem contains meta data of a ruleset.</p>"""
    next_token: NotRequired["aws_sdk_databrew.types.next_token.NextToken"]
    """<p>A token that you can use in a subsequent call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.ruleset_item_list

    out["Rulesets"] = aws_sdk_databrew.types.ruleset_item_list.serialize_json(
        value["rulesets"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesetsResponse:
    out: ListRulesetsResponse = {}  # type: ignore[typeddict-item]
    if "Rulesets" in data:
        import aws_sdk_databrew.types.ruleset_item_list

        out["rulesets"] = aws_sdk_databrew.types.ruleset_item_list.deserialize_json(
            data["Rulesets"]
        )
    else:
        raise DeserializationError("ListRulesetsResponse.rulesets required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
