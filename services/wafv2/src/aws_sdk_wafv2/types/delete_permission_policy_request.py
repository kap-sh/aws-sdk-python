"""Generated from Smithy shape ``com.amazonaws.wafv2#DeletePermissionPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.resource_arn


class DeletePermissionPolicyRequest(TypedDict):
    resource_arn: "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the rule group from which you want to delete the policy.</p> <p>You must be the owner of the rule group to perform this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePermissionPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePermissionPolicyRequest:
    out: DeletePermissionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DeletePermissionPolicyRequest.resource_arn required"
        )
    return out
