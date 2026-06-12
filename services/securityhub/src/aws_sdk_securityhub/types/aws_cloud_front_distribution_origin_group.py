"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover


class AwsCloudFrontDistributionOriginGroup(TypedDict):
    failover_criteria: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover.AwsCloudFrontDistributionOriginGroupFailover"
    ]
    """<p>Provides the criteria for an origin group to fail over.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroup) -> dict:
    out: dict = {}
    if "failover_criteria" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover

        out["FailoverCriteria"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover.serialize_json(
                value["failover_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginGroup:
    out: AwsCloudFrontDistributionOriginGroup = {}  # type: ignore[typeddict-item]
    if "FailoverCriteria" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover

        out["failover_criteria"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_group_failover.deserialize_json(
                data["FailoverCriteria"]
            )
        )
    return out
