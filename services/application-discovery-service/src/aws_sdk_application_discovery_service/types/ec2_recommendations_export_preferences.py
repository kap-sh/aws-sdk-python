"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Ec2RecommendationsExportPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.excluded_instance_types
    import aws_sdk_application_discovery_service.types.export_enabled
    import aws_sdk_application_discovery_service.types.reserved_instance_options
    import aws_sdk_application_discovery_service.types.tenancy
    import aws_sdk_application_discovery_service.types.usage_metric_basis
    import aws_sdk_application_discovery_service.types.user_preferred_region


class Ec2RecommendationsExportPreferences(TypedDict, closed=True):
    enabled: "aws_sdk_application_discovery_service.types.export_enabled.ExportEnabled"
    r"""<p> If set to true, the export <a href=\"https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html#API_StartExportTask_RequestSyntax\">preferences</a> is set to <code>Ec2RecommendationsExportPreferences</code>. </p>"""
    cpu_performance_metric_basis: NotRequired[
        "aws_sdk_application_discovery_service.types.usage_metric_basis.UsageMetricBasis"
    ]
    """<p> The recommended EC2 instance type that matches the CPU usage metric of server performance data. </p>"""
    ram_performance_metric_basis: NotRequired[
        "aws_sdk_application_discovery_service.types.usage_metric_basis.UsageMetricBasis"
    ]
    """<p> The recommended EC2 instance type that matches the Memory usage metric of server performance data. </p>"""
    tenancy: NotRequired["aws_sdk_application_discovery_service.types.tenancy.Tenancy"]
    """<p> The target tenancy to use for your recommended EC2 instances. </p>"""
    excluded_instance_types: NotRequired[
        "aws_sdk_application_discovery_service.types.excluded_instance_types.ExcludedInstanceTypes"
    ]
    """<p> An array of instance types to exclude from recommendations. </p>"""
    preferred_region: NotRequired[
        "aws_sdk_application_discovery_service.types.user_preferred_region.UserPreferredRegion"
    ]
    r"""<p> The target Amazon Web Services Region for the recommendations. You can use any of the Region codes available for the chosen service, as listed in <a href=\"https://docs.aws.amazon.com/general/latest/gr/rande.html\">Amazon Web Services service endpoints</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    reserved_instance_options: NotRequired[
        "aws_sdk_application_discovery_service.types.reserved_instance_options.ReservedInstanceOptions"
    ]
    """<p> The contract type for a reserved instance. If blank, we assume an On-Demand instance is preferred. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2RecommendationsExportPreferences) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "cpu_performance_metric_basis" in value:
        import aws_sdk_application_discovery_service.types.usage_metric_basis

        out["cpuPerformanceMetricBasis"] = (
            aws_sdk_application_discovery_service.types.usage_metric_basis.serialize_aws_json_1_1(
                value["cpu_performance_metric_basis"]
            )
        )
    if "ram_performance_metric_basis" in value:
        import aws_sdk_application_discovery_service.types.usage_metric_basis

        out["ramPerformanceMetricBasis"] = (
            aws_sdk_application_discovery_service.types.usage_metric_basis.serialize_aws_json_1_1(
                value["ram_performance_metric_basis"]
            )
        )
    if "tenancy" in value:
        import aws_sdk_application_discovery_service.types.tenancy

        out["tenancy"] = (
            aws_sdk_application_discovery_service.types.tenancy.serialize_aws_json_1_1(
                value["tenancy"]
            )
        )
    if "excluded_instance_types" in value:
        import aws_sdk_application_discovery_service.types.excluded_instance_types

        out["excludedInstanceTypes"] = (
            aws_sdk_application_discovery_service.types.excluded_instance_types.serialize_aws_json_1_1(
                value["excluded_instance_types"]
            )
        )
    if "preferred_region" in value:
        out["preferredRegion"] = value["preferred_region"]
    if "reserved_instance_options" in value:
        import aws_sdk_application_discovery_service.types.reserved_instance_options

        out["reservedInstanceOptions"] = (
            aws_sdk_application_discovery_service.types.reserved_instance_options.serialize_aws_json_1_1(
                value["reserved_instance_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2RecommendationsExportPreferences:
    out: Ec2RecommendationsExportPreferences = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "cpuPerformanceMetricBasis" in data:
        import aws_sdk_application_discovery_service.types.usage_metric_basis

        out["cpu_performance_metric_basis"] = (
            aws_sdk_application_discovery_service.types.usage_metric_basis.deserialize_aws_json_1_1(
                data["cpuPerformanceMetricBasis"]
            )
        )
    if "ramPerformanceMetricBasis" in data:
        import aws_sdk_application_discovery_service.types.usage_metric_basis

        out["ram_performance_metric_basis"] = (
            aws_sdk_application_discovery_service.types.usage_metric_basis.deserialize_aws_json_1_1(
                data["ramPerformanceMetricBasis"]
            )
        )
    if "tenancy" in data:
        import aws_sdk_application_discovery_service.types.tenancy

        out["tenancy"] = (
            aws_sdk_application_discovery_service.types.tenancy.deserialize_aws_json_1_1(
                data["tenancy"]
            )
        )
    if "excludedInstanceTypes" in data:
        import aws_sdk_application_discovery_service.types.excluded_instance_types

        out["excluded_instance_types"] = (
            aws_sdk_application_discovery_service.types.excluded_instance_types.deserialize_aws_json_1_1(
                data["excludedInstanceTypes"]
            )
        )
    if "preferredRegion" in data:
        out["preferred_region"] = data["preferredRegion"]
    if "reservedInstanceOptions" in data:
        import aws_sdk_application_discovery_service.types.reserved_instance_options

        out["reserved_instance_options"] = (
            aws_sdk_application_discovery_service.types.reserved_instance_options.deserialize_aws_json_1_1(
                data["reservedInstanceOptions"]
            )
        )
    return out
