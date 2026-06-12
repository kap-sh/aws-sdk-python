"""Generated from Smithy shape ``com.amazonaws.wafv2#RegexPatternSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.regular_expression_list
    import aws_sdk_wafv2.types.resource_arn


class RegexPatternSet(TypedDict):
    name: NotRequired["aws_sdk_wafv2.types.entity_name.EntityName"]
    """<p>The name of the set. You cannot change the name after you create the set.</p>"""
    id: NotRequired["aws_sdk_wafv2.types.entity_id.EntityId"]
    """<p>A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    arn: NotRequired["aws_sdk_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the set that helps with identification. </p>"""
    regular_expression_list: NotRequired[
        "aws_sdk_wafv2.types.regular_expression_list.RegularExpressionList"
    ]
    """<p>The regular expression patterns in the set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSet) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "regular_expression_list" in value:
        import aws_sdk_wafv2.types.regular_expression_list

        out["RegularExpressionList"] = (
            aws_sdk_wafv2.types.regular_expression_list.serialize_aws_json_1_1(
                value["regular_expression_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexPatternSet:
    out: RegexPatternSet = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RegularExpressionList" in data:
        import aws_sdk_wafv2.types.regular_expression_list

        out["regular_expression_list"] = (
            aws_sdk_wafv2.types.regular_expression_list.deserialize_aws_json_1_1(
                data["RegularExpressionList"]
            )
        )
    return out
