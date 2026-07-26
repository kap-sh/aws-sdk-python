"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.amazon_q_properties_input
    import capo_datazone.types.athena_properties_input
    import capo_datazone.types.glue_properties_input
    import capo_datazone.types.hyper_pod_properties_input
    import capo_datazone.types.iam_properties_input
    import capo_datazone.types.lakehouse_properties_input
    import capo_datazone.types.mlflow_properties_input
    import capo_datazone.types.redshift_properties_input
    import capo_datazone.types.s3_properties_input
    import capo_datazone.types.spark_emr_properties_input
    import capo_datazone.types.spark_glue_properties_input
    import capo_datazone.types.vpc_properties_input
    import capo_datazone.types.workflows_mwaa_properties_input
    import capo_datazone.types.workflows_serverless_properties_input


class _ConnectionPropertiesInput_athenaProperties(TypedDict, closed=True):
    athenaProperties: (
        "capo_datazone.types.athena_properties_input.AthenaPropertiesInput"
    )


class _ConnectionPropertiesInput_glueProperties(TypedDict, closed=True):
    glueProperties: "capo_datazone.types.glue_properties_input.GluePropertiesInput"


class _ConnectionPropertiesInput_hyperPodProperties(TypedDict, closed=True):
    hyperPodProperties: (
        "capo_datazone.types.hyper_pod_properties_input.HyperPodPropertiesInput"
    )


class _ConnectionPropertiesInput_iamProperties(TypedDict, closed=True):
    iamProperties: "capo_datazone.types.iam_properties_input.IamPropertiesInput"


class _ConnectionPropertiesInput_redshiftProperties(TypedDict, closed=True):
    redshiftProperties: (
        "capo_datazone.types.redshift_properties_input.RedshiftPropertiesInput"
    )


class _ConnectionPropertiesInput_sparkEmrProperties(TypedDict, closed=True):
    sparkEmrProperties: (
        "capo_datazone.types.spark_emr_properties_input.SparkEmrPropertiesInput"
    )


class _ConnectionPropertiesInput_sparkGlueProperties(TypedDict, closed=True):
    sparkGlueProperties: (
        "capo_datazone.types.spark_glue_properties_input.SparkGluePropertiesInput"
    )


class _ConnectionPropertiesInput_s3Properties(TypedDict, closed=True):
    s3Properties: "capo_datazone.types.s3_properties_input.S3PropertiesInput"


class _ConnectionPropertiesInput_amazonQProperties(TypedDict, closed=True):
    amazonQProperties: (
        "capo_datazone.types.amazon_q_properties_input.AmazonQPropertiesInput"
    )


class _ConnectionPropertiesInput_mlflowProperties(TypedDict, closed=True):
    mlflowProperties: (
        "capo_datazone.types.mlflow_properties_input.MlflowPropertiesInput"
    )


class _ConnectionPropertiesInput_workflowsMwaaProperties(TypedDict, closed=True):
    workflowsMwaaProperties: "capo_datazone.types.workflows_mwaa_properties_input.WorkflowsMwaaPropertiesInput"


class _ConnectionPropertiesInput_workflowsServerlessProperties(TypedDict, closed=True):
    workflowsServerlessProperties: "capo_datazone.types.workflows_serverless_properties_input.WorkflowsServerlessPropertiesInput"


class _ConnectionPropertiesInput_lakehouseProperties(TypedDict, closed=True):
    lakehouseProperties: (
        "capo_datazone.types.lakehouse_properties_input.LakehousePropertiesInput"
    )


class _ConnectionPropertiesInput_vpcProperties(TypedDict, closed=True):
    vpcProperties: "capo_datazone.types.vpc_properties_input.VpcPropertiesInput"


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
        import capo_datazone.types.athena_properties_input

        return {
            "athenaProperties": capo_datazone.types.athena_properties_input.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import capo_datazone.types.glue_properties_input

        return {
            "glueProperties": capo_datazone.types.glue_properties_input.serialize_json(
                value["glueProperties"]
            )
        }
    elif "hyperPodProperties" in value:
        import capo_datazone.types.hyper_pod_properties_input

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_input.serialize_json(
                value["hyperPodProperties"]
            )
        }
    elif "iamProperties" in value:
        import capo_datazone.types.iam_properties_input

        return {
            "iamProperties": capo_datazone.types.iam_properties_input.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import capo_datazone.types.redshift_properties_input

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_input.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import capo_datazone.types.spark_emr_properties_input

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_input.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in value:
        import capo_datazone.types.spark_glue_properties_input

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_input.serialize_json(
                value["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in value:
        import capo_datazone.types.s3_properties_input

        return {
            "s3Properties": capo_datazone.types.s3_properties_input.serialize_json(
                value["s3Properties"]
            )
        }
    elif "amazonQProperties" in value:
        import capo_datazone.types.amazon_q_properties_input

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_input.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import capo_datazone.types.mlflow_properties_input

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_input.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in value:
        import capo_datazone.types.workflows_mwaa_properties_input

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_input.serialize_json(
                value["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in value:
        import capo_datazone.types.workflows_serverless_properties_input

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_input.serialize_json(
                value["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import capo_datazone.types.lakehouse_properties_input

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_input.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import capo_datazone.types.vpc_properties_input

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_input.serialize_json(
                value["vpcProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesInput: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesInput:
    if "athenaProperties" in data:
        import capo_datazone.types.athena_properties_input

        return {
            "athenaProperties": capo_datazone.types.athena_properties_input.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif "glueProperties" in data:
        import capo_datazone.types.glue_properties_input

        return {
            "glueProperties": capo_datazone.types.glue_properties_input.deserialize_json(
                data["glueProperties"]
            )
        }
    elif "hyperPodProperties" in data:
        import capo_datazone.types.hyper_pod_properties_input

        return {
            "hyperPodProperties": capo_datazone.types.hyper_pod_properties_input.deserialize_json(
                data["hyperPodProperties"]
            )
        }
    elif "iamProperties" in data:
        import capo_datazone.types.iam_properties_input

        return {
            "iamProperties": capo_datazone.types.iam_properties_input.deserialize_json(
                data["iamProperties"]
            )
        }
    elif "redshiftProperties" in data:
        import capo_datazone.types.redshift_properties_input

        return {
            "redshiftProperties": capo_datazone.types.redshift_properties_input.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in data:
        import capo_datazone.types.spark_emr_properties_input

        return {
            "sparkEmrProperties": capo_datazone.types.spark_emr_properties_input.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif "sparkGlueProperties" in data:
        import capo_datazone.types.spark_glue_properties_input

        return {
            "sparkGlueProperties": capo_datazone.types.spark_glue_properties_input.deserialize_json(
                data["sparkGlueProperties"]
            )
        }
    elif "s3Properties" in data:
        import capo_datazone.types.s3_properties_input

        return {
            "s3Properties": capo_datazone.types.s3_properties_input.deserialize_json(
                data["s3Properties"]
            )
        }
    elif "amazonQProperties" in data:
        import capo_datazone.types.amazon_q_properties_input

        return {
            "amazonQProperties": capo_datazone.types.amazon_q_properties_input.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in data:
        import capo_datazone.types.mlflow_properties_input

        return {
            "mlflowProperties": capo_datazone.types.mlflow_properties_input.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif "workflowsMwaaProperties" in data:
        import capo_datazone.types.workflows_mwaa_properties_input

        return {
            "workflowsMwaaProperties": capo_datazone.types.workflows_mwaa_properties_input.deserialize_json(
                data["workflowsMwaaProperties"]
            )
        }
    elif "workflowsServerlessProperties" in data:
        import capo_datazone.types.workflows_serverless_properties_input

        return {
            "workflowsServerlessProperties": capo_datazone.types.workflows_serverless_properties_input.deserialize_json(
                data["workflowsServerlessProperties"]
            )
        }
    elif "lakehouseProperties" in data:
        import capo_datazone.types.lakehouse_properties_input

        return {
            "lakehouseProperties": capo_datazone.types.lakehouse_properties_input.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in data:
        import capo_datazone.types.vpc_properties_input

        return {
            "vpcProperties": capo_datazone.types.vpc_properties_input.deserialize_json(
                data["vpcProperties"]
            )
        }
    else:
        raise DeserializationError(
            "ConnectionPropertiesInput: no recognized variant key"
        )
