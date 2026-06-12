"""Generated from Smithy shape ``com.amazonaws.databrew#RulesetItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.account_id
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.rule_count
    import aws_sdk_databrew.types.ruleset_description
    import aws_sdk_databrew.types.ruleset_name
    import aws_sdk_databrew.types.tag_map


class RulesetItem(TypedDict):
    account_id: NotRequired["aws_sdk_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the ruleset.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the ruleset.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the ruleset was created.</p>"""
    description: NotRequired[
        "aws_sdk_databrew.types.ruleset_description.RulesetDescription"
    ]
    """<p>The description of the ruleset.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the ruleset.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The modification date and time of the ruleset.</p>"""
    name: "aws_sdk_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the ruleset.</p>"""
    rule_count: "aws_sdk_databrew.types.rule_count.RuleCount"
    """<p>The number of rules that are defined in the ruleset.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the ruleset.</p>"""
    target_arn: "aws_sdk_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RulesetItem) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    out["RuleCount"] = value.get("rule_count", 0)
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    out["TargetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> RulesetItem:
    out: RulesetItem = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RulesetItem.name required")
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RuleCount" in data:
        out["rule_count"] = data["RuleCount"]
    else:
        out["rule_count"] = 0
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError("RulesetItem.target_arn required")
    return out
