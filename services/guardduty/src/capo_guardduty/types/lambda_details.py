"""Generated from Smithy shape ``com.amazonaws.guardduty#LambdaDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.tags
    import capo_guardduty.types.timestamp
    import capo_guardduty.types.vpc_config


class LambdaDetails(TypedDict, closed=True):
    function_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>Amazon Resource Name (ARN) of the Lambda function.</p>"""
    function_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Name of the Lambda function.</p>"""
    description: NotRequired["capo_guardduty.types.string.String"]
    """<p>Description of the Lambda function.</p>"""
    last_modified_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the Lambda function was last modified. This field is in the UTC date string format <code>(2023-03-22T19:37:20.168Z)</code>.</p>"""
    revision_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The revision ID of the Lambda function version.</p>"""
    function_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the Lambda function.</p>"""
    role: NotRequired["capo_guardduty.types.string.String"]
    """<p>The execution role of the Lambda function.</p>"""
    vpc_config: NotRequired["capo_guardduty.types.vpc_config.VpcConfig"]
    """<p>Amazon Virtual Private Cloud configuration details associated with your Lambda function.</p>"""
    tags: NotRequired["capo_guardduty.types.tags.Tags"]
    """<p>A list of tags attached to this resource, listed in the format of <code>key</code>:<code>value</code> pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDetails) -> dict:
    out: dict = {}
    if "function_arn" in value:
        out["functionArn"] = value["function_arn"]
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_modified_at" in value:
        import capo_guardduty.types.timestamp

        out["lastModifiedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["last_modified_at"]
        )
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "function_version" in value:
        out["functionVersion"] = value["function_version"]
    if "role" in value:
        out["role"] = value["role"]
    if "vpc_config" in value:
        import capo_guardduty.types.vpc_config

        out["vpcConfig"] = capo_guardduty.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "tags" in value:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> LambdaDetails:
    out: LambdaDetails = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    if "functionName" in data:
        out["function_name"] = data["functionName"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastModifiedAt" in data:
        import capo_guardduty.types.timestamp

        out["last_modified_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["lastModifiedAt"]
        )
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "functionVersion" in data:
        out["function_version"] = data["functionVersion"]
    if "role" in data:
        out["role"] = data["role"]
    if "vpcConfig" in data:
        import capo_guardduty.types.vpc_config

        out["vpc_config"] = capo_guardduty.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if "tags" in data:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.deserialize_json(data["tags"])
    return out
