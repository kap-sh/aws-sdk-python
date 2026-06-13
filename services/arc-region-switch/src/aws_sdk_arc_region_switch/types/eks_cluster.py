"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.eks_cluster_arn
    import aws_sdk_arc_region_switch.types.iam_role_arn


class EksCluster(TypedDict):
    cross_account_role: NotRequired[
        "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    cluster_arn: "aws_sdk_arc_region_switch.types.eks_cluster_arn.EksClusterArn"
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services EKS cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksCluster) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["clusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EksCluster:
    out: EksCluster = {}  # type: ignore[typeddict-item]
    if "crossAccountRole" in data:
        out["cross_account_role"] = data["crossAccountRole"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("EksCluster.cluster_arn required")
    return out
