"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.rule_groups_namespace_arn
    import aws_sdk_amp.types.rule_groups_namespace_name
    import aws_sdk_amp.types.rule_groups_namespace_status
    import aws_sdk_amp.types.tag_map


class RuleGroupsNamespaceSummary(TypedDict):
    arn: "aws_sdk_amp.types.rule_groups_namespace_arn.RuleGroupsNamespaceArn"
    """<p>The ARN of the rule groups namespace.</p>"""
    name: "aws_sdk_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace.</p>"""
    status: "aws_sdk_amp.types.rule_groups_namespace_status.RuleGroupsNamespaceStatus"
    """<p>A structure that displays the current status of the rule groups namespace.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the rule groups namespace was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time that the rule groups namespace was most recently changed.</p>"""
    tags: NotRequired["aws_sdk_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the rule groups namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_amp.types.rule_groups_namespace_status

    out["status"] = aws_sdk_amp.types.rule_groups_namespace_status.serialize_json(
        value["status"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "tags" in value:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RuleGroupsNamespaceSummary:
    out: RuleGroupsNamespaceSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RuleGroupsNamespaceSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RuleGroupsNamespaceSummary.name required")
    if "status" in data:
        import aws_sdk_amp.types.rule_groups_namespace_status

        out["status"] = aws_sdk_amp.types.rule_groups_namespace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceSummary.status required")
    if "createdAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["created_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceSummary.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["modified_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceSummary.modified_at required")
    if "tags" in data:
        import aws_sdk_amp.types.tag_map

        out["tags"] = aws_sdk_amp.types.tag_map.deserialize_json(data["tags"])
    return out
