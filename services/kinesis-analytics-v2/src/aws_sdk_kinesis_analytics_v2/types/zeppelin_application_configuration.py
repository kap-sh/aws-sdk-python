"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinApplicationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.catalog_configuration
    import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list
    import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration


class ZeppelinApplicationConfiguration(TypedDict):
    monitoring_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration.ZeppelinMonitoringConfiguration"
    ]
    """<p>The monitoring configuration of a Managed Service for Apache Flink Studio notebook.</p>"""
    catalog_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.catalog_configuration.CatalogConfiguration"
    ]
    """<p>The Amazon Glue Data Catalog that you use in queries in a Managed Service for Apache Flink Studio notebook.</p>"""
    deploy_as_application_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration.DeployAsApplicationConfiguration"
    ]
    """<p>The information required to deploy a Managed Service for Apache Flink Studio notebook as an application with durable state.</p>"""
    custom_artifacts_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list.CustomArtifactsConfigurationList"
    ]
    """<p>Custom artifacts are dependency JARs and user-defined functions (UDF).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinApplicationConfiguration) -> dict:
    out: dict = {}
    if "monitoring_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration

        out["MonitoringConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "catalog_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.catalog_configuration

        out["CatalogConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.catalog_configuration.serialize_aws_json_1_1(
                value["catalog_configuration"]
            )
        )
    if "deploy_as_application_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration

        out["DeployAsApplicationConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration.serialize_aws_json_1_1(
                value["deploy_as_application_configuration"]
            )
        )
    if "custom_artifacts_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list

        out["CustomArtifactsConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list.serialize_aws_json_1_1(
                value["custom_artifacts_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinApplicationConfiguration:
    out: ZeppelinApplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "MonitoringConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if "CatalogConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.catalog_configuration

        out["catalog_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.catalog_configuration.deserialize_aws_json_1_1(
                data["CatalogConfiguration"]
            )
        )
    if "DeployAsApplicationConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration

        out["deploy_as_application_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration.deserialize_aws_json_1_1(
                data["DeployAsApplicationConfiguration"]
            )
        )
    if "CustomArtifactsConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list

        out["custom_artifacts_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_list.deserialize_aws_json_1_1(
                data["CustomArtifactsConfiguration"]
            )
        )
    return out
