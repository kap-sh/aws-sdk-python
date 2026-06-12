"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.resource_arn
    import aws_sdk_resource_groups.types.resource_type


class ResourceIdentifier(TypedDict):
    resource_arn: NotRequired["aws_sdk_resource_groups.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of a resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_resource_groups.types.resource_type.ResourceType"
    ]
    """<p>The resource type of a resource, such as <code>AWS::EC2::Instance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdentifier) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceIdentifier:
    out: ResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
