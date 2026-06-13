"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowTransformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration
    import aws_sdk_supplychain.types.data_integration_flow_transformation_type


class DataIntegrationFlowTransformation(TypedDict):
    transformation_type: "aws_sdk_supplychain.types.data_integration_flow_transformation_type.DataIntegrationFlowTransformationType"
    """<p>The DataIntegrationFlow transformation type.</p>"""
    sql_transformation: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration.DataIntegrationFlowSQLTransformationConfiguration"
    ]
    """<p>The SQL DataIntegrationFlow transformation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowTransformation) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow_transformation_type

    out["transformationType"] = (
        aws_sdk_supplychain.types.data_integration_flow_transformation_type.serialize_json(
            value["transformation_type"]
        )
    )
    if "sql_transformation" in value:
        import aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration

        out["sqlTransformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration.serialize_json(
                value["sql_transformation"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowTransformation:
    out: DataIntegrationFlowTransformation = {}  # type: ignore[typeddict-item]
    if "transformationType" in data:
        import aws_sdk_supplychain.types.data_integration_flow_transformation_type

        out["transformation_type"] = (
            aws_sdk_supplychain.types.data_integration_flow_transformation_type.deserialize_json(
                data["transformationType"]
            )
        )
    else:
        raise DeserializationError(
            "DataIntegrationFlowTransformation.transformation_type required"
        )
    if "sqlTransformation" in data:
        import aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration

        out["sql_transformation"] = (
            aws_sdk_supplychain.types.data_integration_flow_sql_transformation_configuration.deserialize_json(
                data["sqlTransformation"]
            )
        )
    return out
