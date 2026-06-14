"""Generated from Smithy shape ``com.amazonaws.eks#CreateFargateProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile_selectors
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.tag_map


class CreateFargateProfileRequest(TypedDict):
    fargate_profile_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Fargate profile.</p>"""
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    pod_execution_role_arn: "aws_sdk_eks.types.string.String"
    r"""<p>The Amazon Resource Name (ARN) of the <code>Pod</code> execution role to use for a <code>Pod</code> that matches the selectors in the Fargate profile. The <code>Pod</code> execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html\"> <code>Pod</code> execution role</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    subnets: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The IDs of subnets to launch a <code>Pod</code> into. A <code>Pod</code> running on Fargate isn't assigned a public IP address, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.</p>"""
    selectors: NotRequired[
        "aws_sdk_eks.types.fargate_profile_selectors.FargateProfileSelectors"
    ]
    """<p>The selectors to match for a <code>Pod</code> to use this Fargate profile. Each selector must have an associated Kubernetes <code>namespace</code>. Optionally, you can also specify <code>labels</code> for a <code>namespace</code>. You may specify up to five selectors in a Fargate profile.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFargateProfileRequest) -> dict:
    out: dict = {}
    out["fargateProfileName"] = value["fargate_profile_name"]
    out["podExecutionRoleArn"] = value["pod_execution_role_arn"]
    if "subnets" in value:
        import aws_sdk_eks.types.string_list

        out["subnets"] = aws_sdk_eks.types.string_list.serialize_json(value["subnets"])
    if "selectors" in value:
        import aws_sdk_eks.types.fargate_profile_selectors

        out["selectors"] = aws_sdk_eks.types.fargate_profile_selectors.serialize_json(
            value["selectors"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFargateProfileRequest:
    out: CreateFargateProfileRequest = {}  # type: ignore[typeddict-item]
    if "fargateProfileName" in data:
        out["fargate_profile_name"] = data["fargateProfileName"]
    else:
        raise DeserializationError(
            "CreateFargateProfileRequest.fargate_profile_name required"
        )
    if "podExecutionRoleArn" in data:
        out["pod_execution_role_arn"] = data["podExecutionRoleArn"]
    else:
        raise DeserializationError(
            "CreateFargateProfileRequest.pod_execution_role_arn required"
        )
    if "subnets" in data:
        import aws_sdk_eks.types.string_list

        out["subnets"] = aws_sdk_eks.types.string_list.deserialize_json(data["subnets"])
    if "selectors" in data:
        import aws_sdk_eks.types.fargate_profile_selectors

        out["selectors"] = aws_sdk_eks.types.fargate_profile_selectors.deserialize_json(
            data["selectors"]
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "tags" in data:
        import aws_sdk_eks.types.tag_map

        out["tags"] = aws_sdk_eks.types.tag_map.deserialize_json(data["tags"])
    return out
