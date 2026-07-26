"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.association_entity_arn


class DeleteAssociationResponse(TypedDict, closed=True):
    source_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The ARN of the source.</p>"""
    destination_arn: NotRequired[
        "capo_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAssociationResponse) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAssociationResponse:
    out: DeleteAssociationResponse = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    return out
