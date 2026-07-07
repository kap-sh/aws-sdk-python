"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.rule_list
    import aws_sdk_databrew.types.ruleset_description
    import aws_sdk_databrew.types.ruleset_name
    import aws_sdk_databrew.types.tag_map


class CreateRulesetRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    description: NotRequired[
        "aws_sdk_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    target_arn: "aws_sdk_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""
    rules: "aws_sdk_databrew.types.rule_list.RuleList"
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to the ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRulesetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TargetArn"] = value["target_arn"]
    import aws_sdk_databrew.types.rule_list

    out["Rules"] = aws_sdk_databrew.types.rule_list.serialize_json(value["rules"])
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRulesetRequest:
    out: CreateRulesetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRulesetRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError("CreateRulesetRequest.target_arn required")
    if "Rules" in data:
        import aws_sdk_databrew.types.rule_list

        out["rules"] = aws_sdk_databrew.types.rule_list.deserialize_json(data["Rules"])
    else:
        raise DeserializationError("CreateRulesetRequest.rules required")
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
