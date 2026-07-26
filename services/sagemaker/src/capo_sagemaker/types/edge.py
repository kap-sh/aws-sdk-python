"""Generated from Smithy shape ``com.amazonaws.sagemaker#Edge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.association_edge_type
    import capo_sagemaker.types.association_entity_arn


class Edge(TypedDict, closed=True):
    source_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source lineage entity of the directed edge.</p>"""
    destination_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination lineage entity of the directed edge.</p>"""
    association_type: NotRequired[
        "capo_sagemaker.types.association_edge_type.AssociationEdgeType"
    ]
    """<p>The type of the Association(Edge) between the source and destination. For example <code>ContributedTo</code>, <code>Produced</code>, or <code>DerivedFrom</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Edge) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "association_type" in value:
        import capo_sagemaker.types.association_edge_type

        out["AssociationType"] = (
            capo_sagemaker.types.association_edge_type.serialize_aws_json_1_1(
                value["association_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Edge:
    out: Edge = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "AssociationType" in data:
        import capo_sagemaker.types.association_edge_type

        out["association_type"] = (
            capo_sagemaker.types.association_edge_type.deserialize_aws_json_1_1(
                data["AssociationType"]
            )
        )
    return out
