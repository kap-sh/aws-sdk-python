"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinApplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list
    import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description


class ZeppelinApplicationConfigurationDescription(TypedDict, closed=True):
    monitoring_configuration_description: "aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description.ZeppelinMonitoringConfigurationDescription"
    """<p>The monitoring configuration of a Managed Service for Apache Flink Studio notebook.</p>"""
    catalog_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description.CatalogConfigurationDescription"
    ]
    """<p>The Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.</p>"""
    deploy_as_application_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description.DeployAsApplicationConfigurationDescription"
    ]
    """<p>The parameters required to deploy a Managed Service for Apache Flink Studio notebook as an application with durable state.</p>"""
    custom_artifacts_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list.CustomArtifactsConfigurationDescriptionList"
    ]
    """<p>Custom artifacts are dependency JARs and user-defined functions (UDF).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinApplicationConfigurationDescription) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description

    out["MonitoringConfigurationDescription"] = (
        aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description.serialize_aws_json_1_1(
            value["monitoring_configuration_description"]
        )
    )
    if "catalog_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description

        out["CatalogConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description.serialize_aws_json_1_1(
                value["catalog_configuration_description"]
            )
        )
    if "deploy_as_application_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description

        out["DeployAsApplicationConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description.serialize_aws_json_1_1(
                value["deploy_as_application_configuration_description"]
            )
        )
    if "custom_artifacts_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list

        out["CustomArtifactsConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list.serialize_aws_json_1_1(
                value["custom_artifacts_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinApplicationConfigurationDescription:
    out: ZeppelinApplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "MonitoringConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description

        out["monitoring_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_monitoring_configuration_description.deserialize_aws_json_1_1(
                data["MonitoringConfigurationDescription"]
            )
        )
    else:
        raise DeserializationError(
            "ZeppelinApplicationConfigurationDescription.monitoring_configuration_description required"
        )
    if "CatalogConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description

        out["catalog_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.catalog_configuration_description.deserialize_aws_json_1_1(
                data["CatalogConfigurationDescription"]
            )
        )
    if "DeployAsApplicationConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description

        out["deploy_as_application_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.deploy_as_application_configuration_description.deserialize_aws_json_1_1(
                data["DeployAsApplicationConfigurationDescription"]
            )
        )
    if "CustomArtifactsConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list

        out["custom_artifacts_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.custom_artifacts_configuration_description_list.deserialize_aws_json_1_1(
                data["CustomArtifactsConfigurationDescription"]
            )
        )
    return out
