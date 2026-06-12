"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExceptionResourceKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit256
    import aws_sdk_config_service.types.string_with_char_limit1024


class RemediationExceptionResourceKey(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The type of a resource.</p>"""
    resource_id: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>The ID of the resource (for example., sg-xxxxxx).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExceptionResourceKey) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationExceptionResourceKey:
    out: RemediationExceptionResourceKey = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out
