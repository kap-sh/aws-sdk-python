"""Generated from Smithy shape ``com.amazonaws.sagemaker#AddAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.association_edge_type
    import aws_sdk_sagemaker.types.association_entity_arn


class AddAssociationRequest(TypedDict):
    source_arn: NotRequired[
        "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The ARN of the source.</p>"""
    destination_arn: NotRequired[
        "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    association_type: NotRequired[
        "aws_sdk_sagemaker.types.association_edge_type.AssociationEdgeType"
    ]
    """<p>The type of association. The following are suggested uses for each type. Amazon SageMaker places no restrictions on their use.</p> <ul> <li> <p>ContributedTo - The source contributed to the destination or had a part in enabling the destination. For example, the training data contributed to the training job.</p> </li> <li> <p>AssociatedWith - The source is connected to the destination. For example, an approval workflow is associated with a model deployment.</p> </li> <li> <p>DerivedFrom - The destination is a modification of the source. For example, a digest output of a channel input for a processing job is derived from the original inputs.</p> </li> <li> <p>Produced - The source generated the destination. For example, a training job produced a model artifact.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAssociationRequest) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "association_type" in value:
        import aws_sdk_sagemaker.types.association_edge_type

        out["AssociationType"] = (
            aws_sdk_sagemaker.types.association_edge_type.serialize_aws_json_1_1(
                value["association_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAssociationRequest:
    out: AddAssociationRequest = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "AssociationType" in data:
        import aws_sdk_sagemaker.types.association_edge_type

        out["association_type"] = (
            aws_sdk_sagemaker.types.association_edge_type.deserialize_aws_json_1_1(
                data["AssociationType"]
            )
        )
    return out
