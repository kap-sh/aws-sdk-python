"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_arn
    import aws_sdk_connectcases.types.case_rule_description
    import aws_sdk_connectcases.types.case_rule_details
    import aws_sdk_connectcases.types.case_rule_id
    import aws_sdk_connectcases.types.case_rule_name
    import aws_sdk_connectcases.types.created_time
    import aws_sdk_connectcases.types.deleted
    import aws_sdk_connectcases.types.last_modified_time
    import aws_sdk_connectcases.types.tags


class GetCaseRuleResponse(TypedDict, closed=True):
    case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""
    name: "aws_sdk_connectcases.types.case_rule_name.CaseRuleName"
    """<p>Name of the case rule.</p>"""
    case_rule_arn: "aws_sdk_connectcases.types.case_rule_arn.CaseRuleArn"
    """<p>The Amazon Resource Name (ARN) of the case rule.</p>"""
    rule: "aws_sdk_connectcases.types.case_rule_details.CaseRuleDetails"
    """<p>Represents what rule type should take place, under what conditions.</p>"""
    description: NotRequired[
        "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
    ]
    """<p>Description of a case rule.</p>"""
    deleted: "aws_sdk_connectcases.types.deleted.Deleted"
    """<p>Indicates whether the resource has been deleted.</p>"""
    created_time: NotRequired["aws_sdk_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp when the resource was created.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp when the resource was created or last modified.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseRuleResponse) -> dict:
    out: dict = {}
    out["caseRuleId"] = value["case_rule_id"]
    out["name"] = value["name"]
    out["caseRuleArn"] = value["case_rule_arn"]
    import aws_sdk_connectcases.types.case_rule_details

    out["rule"] = aws_sdk_connectcases.types.case_rule_details.serialize_json(
        value["rule"]
    )
    if "description" in value:
        out["description"] = value["description"]
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import aws_sdk_connectcases.types.created_time

        out["createdTime"] = aws_sdk_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            aws_sdk_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCaseRuleResponse:
    out: GetCaseRuleResponse = {}  # type: ignore[typeddict-item]
    if "caseRuleId" in data:
        out["case_rule_id"] = data["caseRuleId"]
    else:
        raise DeserializationError("GetCaseRuleResponse.case_rule_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCaseRuleResponse.name required")
    if "caseRuleArn" in data:
        out["case_rule_arn"] = data["caseRuleArn"]
    else:
        raise DeserializationError("GetCaseRuleResponse.case_rule_arn required")
    if "rule" in data:
        import aws_sdk_connectcases.types.case_rule_details

        out["rule"] = aws_sdk_connectcases.types.case_rule_details.deserialize_json(
            data["rule"]
        )
    else:
        raise DeserializationError("GetCaseRuleResponse.rule required")
    if "description" in data:
        out["description"] = data["description"]
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if "createdTime" in data:
        import aws_sdk_connectcases.types.created_time

        out["created_time"] = aws_sdk_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if "lastModifiedTime" in data:
        import aws_sdk_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    return out
