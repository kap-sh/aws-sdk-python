"""Generated from Smithy shape ``com.amazonaws.fms#WebACLHasIncompatibleConfigurationViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_arn


class WebACLHasIncompatibleConfigurationViolation(TypedDict):
    web_acl_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the web ACL. </p>"""
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>Information about the problems that Firewall Manager encountered with the web ACL configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLHasIncompatibleConfigurationViolation) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLHasIncompatibleConfigurationViolation:
    out: WebACLHasIncompatibleConfigurationViolation = {}  # type: ignore[typeddict-item]
    if "WebACLArn" in data:
        out["web_acl_arn"] = data["WebACLArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
