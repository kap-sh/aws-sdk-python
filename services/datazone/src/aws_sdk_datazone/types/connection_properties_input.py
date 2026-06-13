"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.athena_properties_input
    import aws_sdk_datazone.types.glue_properties_input
    import aws_sdk_datazone.types.hyper_pod_properties_input
    import aws_sdk_datazone.types.iam_properties_input
    import aws_sdk_datazone.types.redshift_properties_input
    import aws_sdk_datazone.types.spark_emr_properties_input
    import aws_sdk_datazone.types.spark_glue_properties_input
    import aws_sdk_datazone.types.s3_properties_input
    import aws_sdk_datazone.types.amazon_q_properties_input
    import aws_sdk_datazone.types.mlflow_properties_input
    import aws_sdk_datazone.types.workflows_mwaa_properties_input
    import aws_sdk_datazone.types.workflows_serverless_properties_input
    import aws_sdk_datazone.types.lakehouse_properties_input
    import aws_sdk_datazone.types.vpc_properties_input


class _ConnectionPropertiesInput_athenaProperties(TypedDict):
    athenaProperties: (
        "aws_sdk_datazone.types.athena_properties_input.AthenaPropertiesInput"
    )


class _ConnectionPropertiesInput_glueProperties(TypedDict):
    glueProperties: "aws_sdk_datazone.types.glue_properties_input.GluePropertiesInput"


class _ConnectionPropertiesInput_hyperPodProperties(TypedDict):
    hyperPodProperties: (
        "aws_sdk_datazone.types.hyper_pod_properties_input.HyperPodPropertiesInput"
    )


class _ConnectionPropertiesInput_iamProperties(TypedDict):
    iamProperties: "aws_sdk_datazone.types.iam_properties_input.IamPropertiesInput"


class _ConnectionPropertiesInput_redshiftProperties(TypedDict):
    redshiftProperties: (
        "aws_sdk_datazone.types.redshift_properties_input.RedshiftPropertiesInput"
    )


class _ConnectionPropertiesInput_sparkEmrProperties(TypedDict):
    sparkEmrProperties: (
        "aws_sdk_datazone.types.spark_emr_properties_input.SparkEmrPropertiesInput"
    )


class _ConnectionPropertiesInput_sparkGlueProperties(TypedDict):
    sparkGlueProperties: (
        "aws_sdk_datazone.types.spark_glue_properties_input.SparkGluePropertiesInput"
    )


class _ConnectionPropertiesInput_s3Properties(TypedDict):
    s3Properties: "aws_sdk_datazone.types.s3_properties_input.S3PropertiesInput"


class _ConnectionPropertiesInput_amazonQProperties(TypedDict):
    amazonQProperties: (
        "aws_sdk_datazone.types.amazon_q_properties_input.AmazonQPropertiesInput"
    )


class _ConnectionPropertiesInput_mlflowProperties(TypedDict):
    mlflowProperties: (
        "aws_sdk_datazone.types.mlflow_properties_input.MlflowPropertiesInput"
    )


class _ConnectionPropertiesInput_workflowsMwaaProperties(TypedDict):
    workflowsMwaaProperties: "aws_sdk_datazone.types.workflows_mwaa_properties_input.WorkflowsMwaaPropertiesInput"


class _ConnectionPropertiesInput_workflowsServerlessProperties(TypedDict):
    workflowsServerlessProperties: "aws_sdk_datazone.types.workflows_serverless_properties_input.WorkflowsServerlessPropertiesInput"


class _ConnectionPropertiesInput_lakehouseProperties(TypedDict):
    lakehouseProperties: (
        "aws_sdk_datazone.types.lakehouse_properties_input.LakehousePropertiesInput"
    )


class _ConnectionPropertiesInput_vpcProperties(TypedDict):
    vpcProperties: "aws_sdk_datazone.types.vpc_properties_input.VpcPropertiesInput"


ConnectionPropertiesInput: TypeAlias = (
    _ConnectionPropertiesInput_athenaProperties
    | _ConnectionPropertiesInput_glueProperties
    | _ConnectionPropertiesInput_hyperPodProperties
    | _ConnectionPropertiesInput_iamProperties
    | _ConnectionPropertiesInput_redshiftProperties
    | _ConnectionPropertiesInput_sparkEmrProperties
    | _ConnectionPropertiesInput_sparkGlueProperties
    | _ConnectionPropertiesInput_s3Properties
    | _ConnectionPropertiesInput_amazonQProperties
    | _ConnectionPropertiesInput_mlflowProperties
    | _ConnectionPropertiesInput_workflowsMwaaProperties
    | _ConnectionPropertiesInput_workflowsServerlessProperties
    | _ConnectionPropertiesInput_lakehouseProperties
    | _ConnectionPropertiesInput_vpcProperties
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionPropertiesInput) -> dict:
    if "athenaProperties" in value:
        import aws_sdk_datazone.types.athena_properties_input

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_input.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import aws_sdk_datazone.types.glue_properties_input

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_input.serialize_json(
                value["glueProperties"]
            )
        }
    elif "hyperPodProperties" in value:
        import aws_sdk_datazone.types.hyper_pod_properties_input

        return {
            "hyperPodProperties": aws_sdk_datazone.types.hyper_pod_properties_input.serialize_json(
                value["hyperPodProperties"]
            )
        }
    elif "iamProperties" in value:
        import aws_sdk_datazone.types.iam_properties_input

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_input.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import aws_sdk_datazone.types.redshift_properties_input

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_input.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import aws_sdk_datazone.types.spark_emr_properties_input

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_input.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in value:
        import aws_sdk_datazone.types.spark_glue_properties_input

        return {
            "sparkGlueProperties": aws_sdk_datazone.types.spark_glue_properties_input.serialize_json(
                value["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in value:
        import aws_sdk_datazone.types.s3_properties_input

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_input.serialize_json(
                value["s3Properties"]
            )
        }
    elif "amazonQProperties" in value:
        import aws_sdk_datazone.types.amazon_q_properties_input

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_input.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import aws_sdk_datazone.types.mlflow_properties_input

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_input.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in value:
        import aws_sdk_datazone.types.workflows_mwaa_properties_input

        return {
            "workflowsMwaaProperties": aws_sdk_datazone.types.workflows_mwaa_properties_input.serialize_json(
                value["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in value:
        import aws_sdk_datazone.types.workflows_serverless_properties_input

        return {
            "workflowsServerlessProperties": aws_sdk_datazone.types.workflows_serverless_properties_input.serialize_json(
                value["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import aws_sdk_datazone.types.lakehouse_properties_input

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_input.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import aws_sdk_datazone.types.vpc_properties_input

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_input.serialize_json(
                value["vpcProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesInput: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesInput:
    if "athenaProperties" in data:
        import aws_sdk_datazone.types.athena_properties_input

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_input.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif "glueProperties" in data:
        import aws_sdk_datazone.types.glue_properties_input

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_input.deserialize_json(
                data["glueProperties"]
            )
        }
    elif "hyperPodProperties" in data:
        import aws_sdk_datazone.types.hyper_pod_properties_input

        return {
            "hyperPodProperties": aws_sdk_datazone.types.hyper_pod_properties_input.deserialize_json(
                data["hyperPodProperties"]
            )
        }
    elif "iamProperties" in data:
        import aws_sdk_datazone.types.iam_properties_input

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_input.deserialize_json(
                data["iamProperties"]
            )
        }
    elif "redshiftProperties" in data:
        import aws_sdk_datazone.types.redshift_properties_input

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_input.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in data:
        import aws_sdk_datazone.types.spark_emr_properties_input

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_input.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in data:
        import aws_sdk_datazone.types.spark_glue_properties_input

        return {
            "sparkGlueProperties": aws_sdk_datazone.types.spark_glue_properties_input.deserialize_json(
                data["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in data:
        import aws_sdk_datazone.types.s3_properties_input

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_input.deserialize_json(
                data["s3Properties"]
            )
        }
    elif "amazonQProperties" in data:
        import aws_sdk_datazone.types.amazon_q_properties_input

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_input.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in data:
        import aws_sdk_datazone.types.mlflow_properties_input

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_input.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in data:
        import aws_sdk_datazone.types.workflows_mwaa_properties_input

        return {
            "workflowsMwaaProperties": aws_sdk_datazone.types.workflows_mwaa_properties_input.deserialize_json(
                data["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in data:
        import aws_sdk_datazone.types.workflows_serverless_properties_input

        return {
            "workflowsServerlessProperties": aws_sdk_datazone.types.workflows_serverless_properties_input.deserialize_json(
                data["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in data:
        import aws_sdk_datazone.types.lakehouse_properties_input

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_input.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in data:
        import aws_sdk_datazone.types.vpc_properties_input

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_input.deserialize_json(
                data["vpcProperties"]
            )
        }
    else:
        raise DeserializationError(
            "ConnectionPropertiesInput: no recognized variant key"
        )
