"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.cloud_hsm_arn


class GetResourcePolicyRequest(TypedDict):
    resource_arn: NotRequired["aws_sdk_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"]
    """<p>Amazon Resource Name (ARN) of the resource to which a policy is attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
