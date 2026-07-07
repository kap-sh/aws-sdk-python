"""Generated from Smithy shape ``com.amazonaws.databrew#UpdateRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.rule_list
    import aws_sdk_databrew.types.ruleset_description
    import aws_sdk_databrew.types.ruleset_name


class UpdateRulesetRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be updated.</p>"""
    description: NotRequired[
        "aws_sdk_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    rules: "aws_sdk_databrew.types.rule_list.RuleList"
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRulesetRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_databrew.types.rule_list

    out["Rules"] = aws_sdk_databrew.types.rule_list.serialize_json(value["rules"])
    return out


def deserialize_json(data: dict) -> UpdateRulesetRequest:
    out: UpdateRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_databrew.types.rule_list

        out["rules"] = aws_sdk_databrew.types.rule_list.deserialize_json(data["Rules"])
    else:
        raise DeserializationError("UpdateRulesetRequest.rules required")
    return out
