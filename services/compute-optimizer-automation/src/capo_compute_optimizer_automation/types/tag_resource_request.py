"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.rule_arn
    import capo_compute_optimizer_automation.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the resource to tag. </p>"""
    rule_revision: "int"
    """<p>The revision number of the automation rule to tag. This ensures you're tagging the correct version of the rule.</p>"""
    tags: "capo_compute_optimizer_automation.types.tag_list.TagList"
    """<p> The tags to add to the resource. </p>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["ruleRevision"] = value["rule_revision"]
    import capo_compute_optimizer_automation.types.tag_list

    out["tags"] = (
        capo_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
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
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
