"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the resource to tag. </p>"""
    rule_revision: "int"
    """<p>The revision number of the automation rule to tag. This ensures you're tagging the correct version of the rule.</p>"""
    tags: "aws_sdk_compute_optimizer_automation.types.tag_list.TagList"
    """<p> The tags to add to the resource. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["ruleRevision"] = value["rule_revision"]
    import aws_sdk_compute_optimizer_automation.types.tag_list

    out["tags"] = (
        aws_sdk_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
    else:
        raise DeserializationError("TagResourceRequest.rule_revision required")
    if "tags" in data:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
