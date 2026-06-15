"""Generated from Smithy shape ``com.amazonaws.glue#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn


class GetResourcePolicyRequest(TypedDict):
    resource_arn: NotRequired["aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"]
    r"""<p>The ARN of the Glue resource for which to retrieve the resource policy. If not supplied, the Data Catalog resource policy is returned. Use <code>GetResourcePolicies</code> to view all existing resource policies. For more information see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html\">Specifying Glue Resource ARNs</a>. </p>"""


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
