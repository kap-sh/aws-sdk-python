"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionPropertiesPatch``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.athena_properties_patch
    import aws_sdk_datazone.types.glue_properties_patch
    import aws_sdk_datazone.types.iam_properties_patch
    import aws_sdk_datazone.types.redshift_properties_patch
    import aws_sdk_datazone.types.spark_emr_properties_patch
    import aws_sdk_datazone.types.s3_properties_patch
    import aws_sdk_datazone.types.amazon_q_properties_patch
    import aws_sdk_datazone.types.mlflow_properties_patch
    import aws_sdk_datazone.types.lakehouse_properties_patch
    import aws_sdk_datazone.types.vpc_properties_patch


class _ConnectionPropertiesPatch_athenaProperties(TypedDict):
    athenaProperties: (
        "aws_sdk_datazone.types.athena_properties_patch.AthenaPropertiesPatch"
    )


class _ConnectionPropertiesPatch_glueProperties(TypedDict):
    glueProperties: "aws_sdk_datazone.types.glue_properties_patch.GluePropertiesPatch"


class _ConnectionPropertiesPatch_iamProperties(TypedDict):
    iamProperties: "aws_sdk_datazone.types.iam_properties_patch.IamPropertiesPatch"


class _ConnectionPropertiesPatch_redshiftProperties(TypedDict):
    redshiftProperties: (
        "aws_sdk_datazone.types.redshift_properties_patch.RedshiftPropertiesPatch"
    )


class _ConnectionPropertiesPatch_sparkEmrProperties(TypedDict):
    sparkEmrProperties: (
        "aws_sdk_datazone.types.spark_emr_properties_patch.SparkEmrPropertiesPatch"
    )


class _ConnectionPropertiesPatch_s3Properties(TypedDict):
    s3Properties: "aws_sdk_datazone.types.s3_properties_patch.S3PropertiesPatch"


class _ConnectionPropertiesPatch_amazonQProperties(TypedDict):
    amazonQProperties: (
        "aws_sdk_datazone.types.amazon_q_properties_patch.AmazonQPropertiesPatch"
    )


class _ConnectionPropertiesPatch_mlflowProperties(TypedDict):
    mlflowProperties: (
        "aws_sdk_datazone.types.mlflow_properties_patch.MlflowPropertiesPatch"
    )


class _ConnectionPropertiesPatch_lakehouseProperties(TypedDict):
    lakehouseProperties: (
        "aws_sdk_datazone.types.lakehouse_properties_patch.LakehousePropertiesPatch"
    )


class _ConnectionPropertiesPatch_vpcProperties(TypedDict):
    vpcProperties: "aws_sdk_datazone.types.vpc_properties_patch.VpcPropertiesPatch"


ConnectionPropertiesPatch: TypeAlias = (
    _ConnectionPropertiesPatch_athenaProperties
    | _ConnectionPropertiesPatch_glueProperties
    | _ConnectionPropertiesPatch_iamProperties
    | _ConnectionPropertiesPatch_redshiftProperties
    | _ConnectionPropertiesPatch_sparkEmrProperties
    | _ConnectionPropertiesPatch_s3Properties
    | _ConnectionPropertiesPatch_amazonQProperties
    | _ConnectionPropertiesPatch_mlflowProperties
    | _ConnectionPropertiesPatch_lakehouseProperties
    | _ConnectionPropertiesPatch_vpcProperties
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionPropertiesPatch) -> dict:
    if "athenaProperties" in value:
        import aws_sdk_datazone.types.athena_properties_patch

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_patch.serialize_json(
                value["athenaProperties"]
            )
        }
    elif "glueProperties" in value:
        import aws_sdk_datazone.types.glue_properties_patch

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_patch.serialize_json(
                value["glueProperties"]
            )
        }
    elif "iamProperties" in value:
        import aws_sdk_datazone.types.iam_properties_patch

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_patch.serialize_json(
                value["iamProperties"]
            )
        }
    elif "redshiftProperties" in value:
        import aws_sdk_datazone.types.redshift_properties_patch

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_patch.serialize_json(
                value["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in value:
        import aws_sdk_datazone.types.spark_emr_properties_patch

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_patch.serialize_json(
                value["sparkEmrProperties"]
            )
        }
    elif "s3Properties" in value:
        import aws_sdk_datazone.types.s3_properties_patch

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_patch.serialize_json(
                value["s3Properties"]
            )
        }
    elif "amazonQProperties" in value:
        import aws_sdk_datazone.types.amazon_q_properties_patch

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_patch.serialize_json(
                value["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in value:
        import aws_sdk_datazone.types.mlflow_properties_patch

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_patch.serialize_json(
                value["mlflowProperties"]
            )
        }
    elif "lakehouseProperties" in value:
        import aws_sdk_datazone.types.lakehouse_properties_patch

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_patch.serialize_json(
                value["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in value:
        import aws_sdk_datazone.types.vpc_properties_patch

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_patch.serialize_json(
                value["vpcProperties"]
            )
        }
    else:
        raise SerializationError("ConnectionPropertiesPatch: no variant present")


def deserialize_json(data: dict) -> ConnectionPropertiesPatch:
    if "athenaProperties" in data:
        import aws_sdk_datazone.types.athena_properties_patch

        return {
            "athenaProperties": aws_sdk_datazone.types.athena_properties_patch.deserialize_json(
                data["athenaProperties"]
            )
        }
    elif "glueProperties" in data:
        import aws_sdk_datazone.types.glue_properties_patch

        return {
            "glueProperties": aws_sdk_datazone.types.glue_properties_patch.deserialize_json(
                data["glueProperties"]
            )
        }
    elif "iamProperties" in data:
        import aws_sdk_datazone.types.iam_properties_patch

        return {
            "iamProperties": aws_sdk_datazone.types.iam_properties_patch.deserialize_json(
                data["iamProperties"]
            )
        }
    elif "redshiftProperties" in data:
        import aws_sdk_datazone.types.redshift_properties_patch

        return {
            "redshiftProperties": aws_sdk_datazone.types.redshift_properties_patch.deserialize_json(
                data["redshiftProperties"]
            )
        }
    elif "sparkEmrProperties" in data:
        import aws_sdk_datazone.types.spark_emr_properties_patch

        return {
            "sparkEmrProperties": aws_sdk_datazone.types.spark_emr_properties_patch.deserialize_json(
                data["sparkEmrProperties"]
            )
        }
    elif "s3Properties" in data:
        import aws_sdk_datazone.types.s3_properties_patch

        return {
            "s3Properties": aws_sdk_datazone.types.s3_properties_patch.deserialize_json(
                data["s3Properties"]
            )
        }
    elif "amazonQProperties" in data:
        import aws_sdk_datazone.types.amazon_q_properties_patch

        return {
            "amazonQProperties": aws_sdk_datazone.types.amazon_q_properties_patch.deserialize_json(
                data["amazonQProperties"]
            )
        }
    elif "mlflowProperties" in data:
        import aws_sdk_datazone.types.mlflow_properties_patch

        return {
            "mlflowProperties": aws_sdk_datazone.types.mlflow_properties_patch.deserialize_json(
                data["mlflowProperties"]
            )
        }
    elif "lakehouseProperties" in data:
        import aws_sdk_datazone.types.lakehouse_properties_patch

        return {
            "lakehouseProperties": aws_sdk_datazone.types.lakehouse_properties_patch.deserialize_json(
                data["lakehouseProperties"]
            )
        }
    elif "vpcProperties" in data:
        import aws_sdk_datazone.types.vpc_properties_patch

        return {
            "vpcProperties": aws_sdk_datazone.types.vpc_properties_patch.deserialize_json(
                data["vpcProperties"]
            )
        }
    else:
        raise DeserializationError(
            "ConnectionPropertiesPatch: no recognized variant key"
        )
