"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover


class AwsCloudFrontDistributionOriginGroup(TypedDict, closed=True):
    failover_criteria: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover.AwsCloudFrontDistributionOriginGroupFailover"
    ]
    """<p>Provides the criteria for an origin group to fail over.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroup) -> dict:
    out: dict = {}
    if "failover_criteria" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover

        out["FailoverCriteria"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover.serialize_json(
                value["failover_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginGroup:
    out: AwsCloudFrontDistributionOriginGroup = {}  # type: ignore[typeddict-item]
    if "FailoverCriteria" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover

        out["failover_criteria"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover.deserialize_json(
                data["FailoverCriteria"]
            )
        )
    return out
