"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.association_edge_type
    import capo_sagemaker.types.association_entity_arn
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class AssociationSummary(TypedDict, closed=True):
    source_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The ARN of the source.</p>"""
    destination_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    source_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The source type.</p>"""
    destination_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The destination type.</p>"""
    association_type: NotRequired[
        "capo_sagemaker.types.association_edge_type.AssociationEdgeType"
    ]
    """<p>The type of the association.</p>"""
    source_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the source.</p>"""
    destination_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the destination.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the association was created.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationSummary) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "destination_type" in value:
        out["DestinationType"] = value["destination_type"]
    if "association_type" in value:
        import capo_sagemaker.types.association_edge_type

        out["AssociationType"] = (
            capo_sagemaker.types.association_edge_type.serialize_aws_json_1_1(
                value["association_type"]
            )
        )
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationSummary:
    out: AssociationSummary = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "DestinationType" in data:
        out["destination_type"] = data["DestinationType"]
    if "AssociationType" in data:
        import capo_sagemaker.types.association_edge_type

        out["association_type"] = (
            capo_sagemaker.types.association_edge_type.deserialize_aws_json_1_1(
                data["AssociationType"]
            )
        )
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "CreatedBy" in data:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    return out
