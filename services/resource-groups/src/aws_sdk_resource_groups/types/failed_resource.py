"""Generated from Smithy shape ``com.amazonaws.resourcegroups#FailedResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.error_code
    import aws_sdk_resource_groups.types.error_message
    import aws_sdk_resource_groups.types.resource_arn


class FailedResource(TypedDict):
    resource_arn: NotRequired["aws_sdk_resource_groups.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of the resource that failed to be added or removed.</p>"""
    error_message: NotRequired[
        "aws_sdk_resource_groups.types.error_message.ErrorMessage"
    ]
    """<p>The error message text associated with the failure.</p>"""
    error_code: NotRequired["aws_sdk_resource_groups.types.error_code.ErrorCode"]
    """<p>The error code associated with the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedResource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> FailedResource:
    out: FailedResource = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out
