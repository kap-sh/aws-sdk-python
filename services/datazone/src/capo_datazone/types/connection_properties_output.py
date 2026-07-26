"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.amazon_q_properties_output
    import capo_datazone.types.athena_properties_output
    import capo_datazone.types.glue_properties_output
    import capo_datazone.types.hyper_pod_properties_output
    import capo_datazone.types.iam_properties_output
    import capo_datazone.types.lakehouse_properties_output
    import capo_datazone.types.mlflow_properties_output
    import capo_datazone.types.redshift_properties_output
    import capo_datazone.types.s3_properties_output
    import capo_datazone.types.spark_emr_properties_output
    import capo_datazone.types.spark_glue_properties_output
    import capo_datazone.types.vpc_properties_output
    import capo_datazone.types.workflows_mwaa_properties_output
    import capo_datazone.types.workflows_serverless_properties_output


class _ConnectionPropertiesOutput_athenaProperties(TypedDict, closed=True):
    athenaProperties: (
        "capo_datazone.types.athena_properties_output.AthenaPropertiesOutput"
    )


class _ConnectionPropertiesOutput_glueProperties(TypedDict, closed=True):
    glueProperties: "capo_datazone.types.glue_properties_output.GluePropertiesOutput"


class _ConnectionPropertiesOutput_hyperPodProperties(TypedDict, closed=True):
    hyperPodProperties: (
        "capo_datazone.types.hyper_pod_properties_output.HyperPodPropertiesOutput"
    )


class _ConnectionPropertiesOutput_iamProperties(TypedDict, closed=True):
    iamProperties: "capo_datazone.types.iam_properties_output.IamPropertiesOutput"


class _ConnectionPropertiesOutput_redshiftProperties(TypedDict, closed=True):
    redshiftProperties: (
        "capo_datazone.types.redshift_properties_output.RedshiftPropertiesOutput"
    )


class _ConnectionPropertiesOutput_sparkEmrProperties(TypedDict, closed=True):
    sparkEmrProperties: (
        "capo_datazone.types.spark_emr_properties_output.SparkEmrPropertiesOutput"
    )


class _ConnectionPropertiesOutput_sparkGlueProperties(TypedDict, closed=True):
    sparkGlueProperties: (
        "capo_datazone.types.spark_glue_properties_output.SparkGluePropertiesOutput"
    )


class _ConnectionPropertiesOutput_s3Properties(TypedDict, closed=True):
    s3Properties: "capo_datazone.types.s3_properties_output.S3PropertiesOutput"


class _ConnectionPropertiesOutput_amazonQProperties(TypedDict, closed=True):
    amazonQProperties: (
        "capo_datazone.types.amazon_q_properties_output.AmazonQPropertiesOutput"
    )


class _ConnectionPropertiesOutput_mlflowProperties(TypedDict, closed=True):
    mlflowProperties: (
        "capo_datazone.types.mlflow_properties_output.MlflowPropertiesOutput"
    )


class _ConnectionPropertiesOutput_workflowsMwaaProperties(TypedDict, closed=True):
    workflowsMwaaProperties: "capo_datazone.types.workflows_mwaa_properties_output.WorkflowsMwaaPropertiesOutput"


class _ConnectionPropertiesOutput_workflowsServerlessProperties(TypedDict, closed=True):
    workflowsServerlessProperties: "capo_datazone.types.workflows_serverless_properties_output.WorkflowsServerlessPropertiesOutput"


class _ConnectionPropertiesOutput_lakehouseProperties(TypedDict, closed=True):
    lakehouseProperties: (
        "capo_datazone.types.lakehouse_properties_output.LakehousePropertiesOutput"
    )


class _ConnectionPropertiesOutput_vpcProperties(TypedDict, closed=True):
    vpcProperties: "capo_datazone.types.vpc_properties_output.VpcPropertiesOutput"


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
        import capo_datazone.types.athena_properties_output

        return {
            "athenaProperties": capo_datazone.types.athena_properties_output.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import capo_datazone.types.glue_properties_output

        return {
            "glueProperties": capo_datazone.types.glue_properties_output.serialize_json(
                value["glueProperties"]
            )
        }
    elif "hyperPodProperties" in value:
        import capo_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_output.serialize_json(
                value["hyperPodProperties"]
            )
        }
    elif "iamProperties" in value:
        import capo_datazone.types.iam_properties_output

        return {
            "iamProperties": capo_datazone.types.iam_properties_output.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_output.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import capo_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_output.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in value:
        import capo_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_output.serialize_json(
                value["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in value:
        import capo_datazone.types.s3_properties_output

        return {
            "s3Properties": capo_datazone.types.s3_properties_output.serialize_json(
                value["s3Properties"]
            )
        }
    elif "amazonQProperties" in value:
        import capo_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_output.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import capo_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_output.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in value:
        import capo_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_output.serialize_json(
                value["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in value:
        import capo_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_output.serialize_json(
                value["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import capo_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_output.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import capo_datazone.types.vpc_properties_output

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_output.serialize_json(
                value["vpcProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesOutput: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesOutput:
    if "athenaProperties" in data:
        import capo_datazone.types.athena_properties_output

        return {
            "athenaProperties": capo_datazone.types.athena_properties_output.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif "glueProperties" in data:
        import capo_datazone.types.glue_properties_output

        return {
            "glueProperties": capo_datazone.types.glue_properties_output.deserialize_json(
                data["glueProperties"]
            )
        }
    elif "hyperPodProperties" in data:
        import capo_datazone.types.hyper_pod_properties_output

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_output.deserialize_json(
                data["hyperPodProperties"]
            )
        }
    elif "iamProperties" in data:
        import capo_datazone.types.iam_properties_output

        return {
            "iamProperties": capo_datazone.types.iam_properties_output.deserialize_json(
                data["iamProperties"]
            )
        }
    elif "redshiftProperties" in data:
        import capo_datazone.types.redshift_properties_output

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_output.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in data:
        import capo_datazone.types.spark_emr_properties_output

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_output.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in data:
        import capo_datazone.types.spark_glue_properties_output

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_output.deserialize_json(
                data["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in data:
        import capo_datazone.types.s3_properties_output

        return {
            "s3Properties": capo_datazone.types.s3_properties_output.deserialize_json(
                data["s3Properties"]
            )
        }
    elif "amazonQProperties" in data:
        import capo_datazone.types.amazon_q_properties_output

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_output.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in data:
        import capo_datazone.types.mlflow_properties_output

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_output.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in data:
        import capo_datazone.types.workflows_mwaa_properties_output

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_output.deserialize_json(
                data["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in data:
        import capo_datazone.types.workflows_serverless_properties_output

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_output.deserialize_json(
                data["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in data:
        import capo_datazone.types.lakehouse_properties_output

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_output.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in data:
        import capo_datazone.types.vpc_properties_output

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_output.deserialize_json(
                data["vpcProperties"]
            )
        }
    else:
        raise DeserializationError(
            "ConnectionPropertiesOutput: no recognized variant key"
        )
