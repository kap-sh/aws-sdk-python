"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbClusterMember(TypedDict, closed=True):
    is_cluster_writer: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the cluster member is the primary instance for the DB cluster.</p>"""
    promotion_tier: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Specifies the order in which an Aurora replica is promoted to the primary instance when the existing primary instance fails.</p>"""
    db_instance_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The instance identifier for this member of the DB cluster.</p>"""
    db_cluster_parameter_group_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the DB cluster parameter group for this member of the DB cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterMember) -> dict:
    out: dict = {}
    if "is_cluster_writer" in value:
        out["IsClusterWriter"] = value["is_cluster_writer"]
    if "promotion_tier" in value:
        out["PromotionTier"] = value["promotion_tier"]
    if "db_instance_identifier" in value:
        out["DbInstanceIdentifier"] = value["db_instance_identifier"]
    if "db_cluster_parameter_group_status" in value:
        out["DbClusterParameterGroupStatus"] = value[
            "db_cluster_parameter_group_status"
        ]
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterMember:
    out: AwsRdsDbClusterMember = {}  # type: ignore[typeddict-item]
    if "IsClusterWriter" in data:
        out["is_cluster_writer"] = data["IsClusterWriter"]
    if "PromotionTier" in data:
        out["promotion_tier"] = data["PromotionTier"]
    if "DbInstanceIdentifier" in data:
        out["db_instance_identifier"] = data["DbInstanceIdentifier"]
    if "DbClusterParameterGroupStatus" in data:
        out["db_cluster_parameter_group_status"] = data["DbClusterParameterGroupStatus"]
    return out
