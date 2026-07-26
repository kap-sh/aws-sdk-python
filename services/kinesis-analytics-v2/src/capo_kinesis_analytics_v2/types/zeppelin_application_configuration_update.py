"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinApplicationConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.catalog_configuration_update
    import capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list
    import capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update
    import capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update


class ZeppelinApplicationConfigurationUpdate(TypedDict, closed=True):
    monitoring_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update.ZeppelinMonitoringConfigurationUpdate"
    ]
    """<p>Updates to the monitoring configuration of a Managed Service for Apache Flink Studio notebook.</p>"""
    catalog_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.catalog_configuration_update.CatalogConfigurationUpdate"
    ]
    """<p>Updates to the configuration of the Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.</p>"""
    deploy_as_application_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update.DeployAsApplicationConfigurationUpdate"
    ]
    custom_artifacts_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list.CustomArtifactsConfigurationList"
    ]
    """<p>Updates to the customer artifacts. Custom artifacts are dependency JAR files and user-defined functions (UDF).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinApplicationConfigurationUpdate) -> dict:
    out: dict = {}
    if "monitoring_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update

        out["MonitoringConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update.serialize_aws_json_1_1(
                value["monitoring_configuration_update"]
            )
        )
    if "catalog_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.catalog_configuration_update

        out["CatalogConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.catalog_configuration_update.serialize_aws_json_1_1(
                value["catalog_configuration_update"]
            )
        )
    if "deploy_as_application_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update

        out["DeployAsApplicationConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update.serialize_aws_json_1_1(
                value["deploy_as_application_configuration_update"]
            )
        )
    if "custom_artifacts_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list

        out["CustomArtifactsConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list.serialize_aws_json_1_1(
                value["custom_artifacts_configuration_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinApplicationConfigurationUpdate:
    out: ZeppelinApplicationConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "MonitoringConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update

        out["monitoring_configuration_update"] = (
            capo_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_update.deserialize_aws_json_1_1(
                data["MonitoringConfigurationUpdate"]
            )
        )
    if "CatalogConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.catalog_configuration_update

        out["catalog_configuration_update"] = (
            capo_kinesis_analytics_v2.types.catalog_configuration_update.deserialize_aws_json_1_1(
                data["CatalogConfigurationUpdate"]
            )
        )
    if "DeployAsApplicationConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update

        out["deploy_as_application_configuration_update"] = (
            capo_kinesis_analytics_v2.types.deploy_as_application_configuration_update.deserialize_aws_json_1_1(
                data["DeployAsApplicationConfigurationUpdate"]
            )
        )
    if "CustomArtifactsConfigurationUpdate" in data:
        import capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list

        out["custom_artifacts_configuration_update"] = (
            capo_kinesis_analytics_v2.types.custom_artifacts_configuration_list.deserialize_aws_json_1_1(
                data["CustomArtifactsConfigurationUpdate"]
            )
        )
    return out
