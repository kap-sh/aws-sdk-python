"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ResourcePolicy``."""

from typing_extensions import NotRequired, TypedDict


class ResourcePolicy(TypedDict, closed=True):
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    policy: NotRequired["str"]
    """<p>The resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicy) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
