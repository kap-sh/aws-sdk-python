"""Generated from Smithy shape ``com.amazonaws.resourcegroups#PendingResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.resource_arn


class PendingResource(TypedDict):
    resource_arn: NotRequired["aws_sdk_resource_groups.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of the resource that's in a pending state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingResource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PendingResource:
    out: PendingResource = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
