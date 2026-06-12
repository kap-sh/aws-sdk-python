"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id
    import aws_sdk_compute_optimizer.types.last_refresh_timestamp
    import aws_sdk_compute_optimizer.types.license_configuration
    import aws_sdk_compute_optimizer.types.license_finding
    import aws_sdk_compute_optimizer.types.license_finding_reason_codes
    import aws_sdk_compute_optimizer.types.license_recommendation_options
    import aws_sdk_compute_optimizer.types.look_back_period_in_days
    import aws_sdk_compute_optimizer.types.resource_arn
    import aws_sdk_compute_optimizer.types.tags


class LicenseRecommendation(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_compute_optimizer.types.resource_arn.ResourceArn"
    ]
    """<p> The ARN that identifies the Amazon EC2 instance. </p>"""
    account_id: NotRequired["aws_sdk_compute_optimizer.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID of the license. </p>"""
    current_license_configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.license_configuration.LicenseConfiguration"
    ]
    """<p> An object that describes the current configuration of an instance that runs on a license. </p>"""
    lookback_period_in_days: (
        "aws_sdk_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p> The number of days for which utilization metrics were analyzed for an instance that runs on a license. </p>"""
    last_refresh_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p> The timestamp of when the license recommendation was last generated. </p>"""
    finding: NotRequired[
        "aws_sdk_compute_optimizer.types.license_finding.LicenseFinding"
    ]
    """<p> The finding classification for an instance that runs on a license. </p> <p>Findings include:</p> <ul> <li> <p> <code>InsufficentMetrics</code> — When Compute Optimizer detects that your CloudWatch Application Insights isn't enabled or is enabled with insufficient permissions. </p> </li> <li> <p> <code>NotOptimized</code> — When Compute Optimizer detects that your EC2 infrastructure isn't using any of the SQL server license features you're paying for, a license is considered not optimized.</p> </li> <li> <p> <code>Optimized</code> — When Compute Optimizer detects that all specifications of your license meet the performance requirements of your workload. </p> </li> </ul>"""
    finding_reason_codes: NotRequired[
        "aws_sdk_compute_optimizer.types.license_finding_reason_codes.LicenseFindingReasonCodes"
    ]
    """<p> The reason for the finding classification for an instance that runs on a license. </p> <p>Finding reason codes include:</p> <ul> <li> <p> <code>Optimized</code> — All specifications of your license meet the performance requirements of your workload. </p> </li> <li> <p> <code>LicenseOverprovisioned</code> — A license is considered over-provisioned when your license can be downgraded while still meeting the performance requirements of your workload.</p> </li> <li> <p> <code>InvalidCloudwatchApplicationInsights</code> — CloudWatch Application Insights isn't configured properly.</p> </li> <li> <p> <code>CloudwatchApplicationInsightsError</code> — There is a CloudWatch Application Insights error. </p> </li> </ul>"""
    license_recommendation_options: NotRequired[
        "aws_sdk_compute_optimizer.types.license_recommendation_options.LicenseRecommendationOptions"
    ]
    """<p> An array of objects that describe the license recommendation options. </p>"""
    tags: NotRequired["aws_sdk_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to an EC2 instance. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "current_license_configuration" in value:
        import aws_sdk_compute_optimizer.types.license_configuration

        out["currentLicenseConfiguration"] = (
            aws_sdk_compute_optimizer.types.license_configuration.serialize_aws_json_1_0(
                value["current_license_configuration"]
            )
        )
    out["lookbackPeriodInDays"] = value.get("lookback_period_in_days", 0)
    if "last_refresh_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "finding" in value:
        import aws_sdk_compute_optimizer.types.license_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.license_finding.serialize_aws_json_1_0(
                value["finding"]
            )
        )
    if "finding_reason_codes" in value:
        import aws_sdk_compute_optimizer.types.license_finding_reason_codes

        out["findingReasonCodes"] = (
            aws_sdk_compute_optimizer.types.license_finding_reason_codes.serialize_aws_json_1_0(
                value["finding_reason_codes"]
            )
        )
    if "license_recommendation_options" in value:
        import aws_sdk_compute_optimizer.types.license_recommendation_options

        out["licenseRecommendationOptions"] = (
            aws_sdk_compute_optimizer.types.license_recommendation_options.serialize_aws_json_1_0(
                value["license_recommendation_options"]
            )
        )
    if "tags" in value:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseRecommendation:
    out: LicenseRecommendation = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "currentLicenseConfiguration" in data:
        import aws_sdk_compute_optimizer.types.license_configuration

        out["current_license_configuration"] = (
            aws_sdk_compute_optimizer.types.license_configuration.deserialize_aws_json_1_0(
                data["currentLicenseConfiguration"]
            )
        )
    if "lookbackPeriodInDays" in data:
        out["lookback_period_in_days"] = data["lookbackPeriodInDays"]
    else:
        out["lookback_period_in_days"] = 0
    if "lastRefreshTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if "finding" in data:
        import aws_sdk_compute_optimizer.types.license_finding

        out["finding"] = (
            aws_sdk_compute_optimizer.types.license_finding.deserialize_aws_json_1_0(
                data["finding"]
            )
        )
    if "findingReasonCodes" in data:
        import aws_sdk_compute_optimizer.types.license_finding_reason_codes

        out["finding_reason_codes"] = (
            aws_sdk_compute_optimizer.types.license_finding_reason_codes.deserialize_aws_json_1_0(
                data["findingReasonCodes"]
            )
        )
    if "licenseRecommendationOptions" in data:
        import aws_sdk_compute_optimizer.types.license_recommendation_options

        out["license_recommendation_options"] = (
            aws_sdk_compute_optimizer.types.license_recommendation_options.deserialize_aws_json_1_0(
                data["licenseRecommendationOptions"]
            )
        )
    if "tags" in data:
        import aws_sdk_compute_optimizer.types.tags

        out["tags"] = aws_sdk_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
