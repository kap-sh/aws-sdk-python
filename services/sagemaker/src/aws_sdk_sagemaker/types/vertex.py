"""Generated from Smithy shape ``com.amazonaws.sagemaker#Vertex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.association_entity_arn
    import aws_sdk_sagemaker.types.lineage_type
    import aws_sdk_sagemaker.types.string40


class Vertex(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lineage entity resource.</p>"""
    type: NotRequired["aws_sdk_sagemaker.types.string40.String40"]
    """<p>The type of the lineage entity resource. For example: <code>DataSet</code>, <code>Model</code>, <code>Endpoint</code>, etc...</p>"""
    lineage_type: NotRequired["aws_sdk_sagemaker.types.lineage_type.LineageType"]
    """<p>The type of resource of the lineage entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Vertex) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "lineage_type" in value:
        import aws_sdk_sagemaker.types.lineage_type

        out["LineageType"] = (
            aws_sdk_sagemaker.types.lineage_type.serialize_aws_json_1_1(
                value["lineage_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Vertex:
    out: Vertex = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "LineageType" in data:
        import aws_sdk_sagemaker.types.lineage_type

        out["lineage_type"] = (
            aws_sdk_sagemaker.types.lineage_type.deserialize_aws_json_1_1(
                data["LineageType"]
            )
        )
    return out
