"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroupFailover``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes


class AwsCloudFrontDistributionOriginGroupFailover(TypedDict, closed=True):
    status_codes: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes.AwsCloudFrontDistributionOriginGroupFailoverStatusCodes"
    ]
    """<p>Information about the status codes that cause an origin group to fail over.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroupFailover) -> dict:
    out: dict = {}
    if "status_codes" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes

        out["StatusCodes"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes.serialize_json(
                value["status_codes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginGroupFailover:
    out: AwsCloudFrontDistributionOriginGroupFailover = {}  # type: ignore[typeddict-item]
    if "StatusCodes" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes

        out["status_codes"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes.deserialize_json(
                data["StatusCodes"]
            )
        )
    return out
