"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesOutput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.amazon_q_properties_output
    import aws_sdk_datazone.types.athena_properties_output
    import aws_sdk_datazone.types.glue_properties_output
    import aws_sdk_datazone.types.hyper_pod_properties_output
    import aws_sdk_datazone.types.iam_properties_output
    import aws_sdk_datazone.types.lakehouse_properties_output
    import aws_sdk_datazone.types.mlflow_properties_output
    import aws_sdk_datazone.types.redshift_properties_output
    import aws_sdk_datazone.types.s3_properties_output
    import aws_sdk_datazone.types.spark_emr_properties_output
    import aws_sdk_datazone.types.spark_glue_properties_output
    import aws_sdk_datazone.types.vpc_properties_output
    import aws_sdk_datazone.types.workflows_mwaa_properties_output
    import aws_sdk_datazone.types.workflows_serverless_properties_output


class _ConnectionPropertiesOutput_athenaProperties(TypedDict):
    athenaProperties: (
        "aws_sdk_datazone.types.athena_properties_output.AthenaPropertiesOutput"
    )


class _ConnectionPropertiesOutput_glueProperties(TypedDict):
    glueProperties: "aws_sdk_datazone.types.glue_properties_output.GluePropertiesOutput"


class _ConnectionPropertiesOutput_hyperPodProperties(TypedDict):
    hyperPodProperties: (
        "aws_sdk_datazone.types.hyper_pod_properties_output.HyperPodPropertiesOutput"
    )


class _ConnectionPropertiesOutput_iamProperties(TypedDict):
    iamProperties: "aws_sdk_datazone.types.iam_properties_output.IamPropertiesOutput"


class _ConnectionPropertiesOutput_redshiftProperties(TypedDict):
    redshiftProperties: (
        "aws_sdk_datazone.types.redshift_properties_output.RedshiftPropertiesOutput"
    )


class _ConnectionPropertiesOutput_sparkEmrProperties(TypedDict):
    sparkEmrProperties: (
        "aws_sdk_datazone.types.spark_emr_properties_output.SparkEmrPropertiesOutput"
    )


class _ConnectionPropertiesOutput_sparkGlueProperties(TypedDict):
    sparkGlueProperties: (
        "aws_sdk_datazone.types.spark_glue_properties_output.SparkGluePropertiesOutput"
    )


class _ConnectionPropertiesOutput_s3Properties(TypedDict):
    s3Properties: "aws_sdk_datazone.types.s3_properties_output.S3PropertiesOutput"


class _ConnectionPropertiesOutput_amazonQProperties(TypedDict):
    amazonQProperties: (
        "aws_sdk_datazone.types.amazon_q_properties_output.AmazonQPropertiesOutput"
    )


class _ConnectionPropertiesOutput_mlflowProperties(TypedDict):
    mlflowProperties: (
        "aws_sdk_datazone.types.mlflow_properties_output.MlflowPropertiesOutput"
    )


class _ConnectionPropertiesOutput_workflowsMwaaProperties(TypedDict):
    workflowsMwaaProperties: "aws_sdk_datazone.types.workflows_mwaa_properties_output.WorkflowsMwaaPropertiesOutput"


class _ConnectionPropertiesOutput_workflowsServerlessProperties(TypedDict):
    workflowsServerlessProperties: "aws_sdk_datazone.types.workflows_serverless_properties_output.WorkflowsServerlessPropertiesOutput"


class _ConnectionPropertiesOutput_lakehouseProperties(TypedDict):
    lakehouseProperties: (
        "aws_sdk_datazone.types.lakehouse_properties_output.LakehousePropertiesOutput"
    )


class _ConnectionPropertiesOutput_vpcProperties(TypedDict):
    vpcProperties: "aws_sdk_datazone.types.vpc_properties_output.VpcPropertiesOutput"


ConnectionPropertiesOutput: TypeAlias = (
    _ConnectionPropertiesOutput_athenaProperties
    | _ConnectionPropertiesOutput_glueProperties
    | _ConnectionPropertiesOutput_hyperPodProperties
    | _ConnectionPropertiesOutput_iamProperties
    | _ConnectionPropertiesOutput_redshiftProperties
    | _ConnectionPropertiesOutput_sparkEmrProperties
    | _ConnectionPropertiesOutput_sparkGlueProperties
    | _ConnectionPropertiesOutput_s3Properties
    | _ConnectionPropertiesOutput_amazonQProperties
    | _ConnectionPropertiesOutput_mlflowProperties
    | _ConnectionPropertiesOutput_workflowsMwaaProperties
    | _ConnectionPropertiesOutput_workflowsServerlessProperties
    | _ConnectionPropertiesOutput_lakehouseProperties
    | _ConnectionPropertiesOutput_vpcProperties
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionPropertiesOutput) -> dict:
    if "athenaProperties" in value:
        import aws_sdk_datazone.types.athena_properties_output

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_output.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import aws_sdk_datazone.types.glue_properties_output

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_output.serialize_json(
                value["glueProperties"]
            )
        }
    elif "hyperPodProperties" in value:
        import aws_sdk_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": aws_sdk_datazone.types.hyper_pod_properties_output.serialize_json(
                value["hyperPodProperties"]
            )
        }
    elif "iamProperties" in value:
        import aws_sdk_datazone.types.iam_properties_output

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_output.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import aws_sdk_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_output.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import aws_sdk_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_output.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in value:
        import aws_sdk_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": aws_sdk_datazone.types.spark_glue_properties_output.serialize_json(
                value["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in value:
        import aws_sdk_datazone.types.s3_properties_output

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_output.serialize_json(
                value["s3Properties"]
            )
        }
    elif "amazonQProperties" in value:
        import aws_sdk_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_output.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import aws_sdk_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_output.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in value:
        import aws_sdk_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": aws_sdk_datazone.types.workflows_mwaa_properties_output.serialize_json(
                value["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in value:
        import aws_sdk_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": aws_sdk_datazone.types.workflows_serverless_properties_output.serialize_json(
                value["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import aws_sdk_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_output.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import aws_sdk_datazone.types.vpc_properties_output

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_output.serialize_json(
                value["vpcProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesOutput: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesOutput:
    if "athenaProperties" in data:
        import aws_sdk_datazone.types.athena_properties_output

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_output.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif "glueProperties" in data:
        import aws_sdk_datazone.types.glue_properties_output

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_output.deserialize_json(
                data["glueProperties"]
            )
        }
    elif "hyperPodProperties" in data:
        import aws_sdk_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": aws_sdk_datazone.types.hyper_pod_properties_output.deserialize_json(
                data["hyperPodProperties"]
            )
        }
    elif "iamProperties" in data:
        import aws_sdk_datazone.types.iam_properties_output

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_output.deserialize_json(
                data["iamProperties"]
            )
        }
    elif "redshiftProperties" in data:
        import aws_sdk_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_output.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in data:
        import aws_sdk_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_output.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in data:
        import aws_sdk_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": aws_sdk_datazone.types.spark_glue_properties_output.deserialize_json(
                data["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in data:
        import aws_sdk_datazone.types.s3_properties_output

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_output.deserialize_json(
                data["s3Properties"]
            )
        }
    elif "amazonQProperties" in data:
        import aws_sdk_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_output.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in data:
        import aws_sdk_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_output.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in data:
        import aws_sdk_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": aws_sdk_datazone.types.workflows_mwaa_properties_output.deserialize_json(
                data["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in data:
        import aws_sdk_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": aws_sdk_datazone.types.workflows_serverless_properties_output.deserialize_json(
                data["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in data:
        import aws_sdk_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_output.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in data:
        import aws_sdk_datazone.types.vpc_properties_output

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_output.deserialize_json(
                data["vpcProperties"]
            )
        }
    else:
        raise DeserializationError(
            "ConnectionPropertiesOutput: no recognized variant key"
        )
