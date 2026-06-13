"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the resource to untag. </p>"""
    rule_revision: "int"
    """<p>The revision number of the automation rule to untag. This ensures you're untagging the correct version of the rule.</p>"""
    tag_keys: "aws_sdk_compute_optimizer_automation.types.tag_key_list.TagKeyList"
    """<p> The keys of the tags to remove from the resource. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["ruleRevision"] = value["rule_revision"]
    import aws_sdk_compute_optimizer_automation.types.tag_key_list

    out["tagKeys"] = (
        aws_sdk_compute_optimizer_automation.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
    else:
        raise DeserializationError("UntagResourceRequest.rule_revision required")
    if "tagKeys" in data:
        import aws_sdk_compute_optimizer_automation.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_compute_optimizer_automation.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
