"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.rule_list
    import aws_sdk_databrew.types.ruleset_description
    import aws_sdk_databrew.types.ruleset_name
    import aws_sdk_databrew.types.tag_map


class DescribeRulesetResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset.</p>"""
    description: NotRequired[
        "aws_sdk_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    target_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""
    rules: NotRequired["aws_sdk_databrew.types.rule_list.RuleList"]
    """<p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the ruleset was created.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the ruleset.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the ruleset.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The modification date and time of the ruleset.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the ruleset.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRulesetResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "rules" in value:
        import aws_sdk_databrew.types.rule_list

        out["Rules"] = aws_sdk_databrew.types.rule_list.serialize_json(value["rules"])
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeRulesetResponse:
    out: DescribeRulesetResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeRulesetResponse.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    if "Rules" in data:
        import aws_sdk_databrew.types.rule_list

        out["rules"] = aws_sdk_databrew.types.rule_list.deserialize_json(data["Rules"])
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
