"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAcceleratorAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string


class ElasticInferenceAcceleratorAssociation(TypedDict, closed=True):
    elastic_inference_accelerator_arn: NotRequired["capo_ec2.types.string.String"]
    """<p> The Amazon Resource Name (ARN) of the elastic inference accelerator. </p>"""
    elastic_inference_accelerator_association_id: NotRequired[
        "capo_ec2.types.string.String"
    ]
    """<p> The ID of the association. </p>"""
    elastic_inference_accelerator_association_state: NotRequired[
        "capo_ec2.types.string.String"
    ]
    """<p> The state of the elastic inference accelerator. </p>"""
    elastic_inference_accelerator_association_time: NotRequired[
        "capo_ec2.types.date_time.DateTime"
    ]
    """<p> The time at which the elastic inference accelerator is associated with an instance. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticInferenceAcceleratorAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "elastic_inference_accelerator_arn" in value:
        pairs.append(
            (
                f"{prefix}.ElasticInferenceAcceleratorArn",
                str(value["elastic_inference_accelerator_arn"]),
            )
        )
    if "elastic_inference_accelerator_association_id" in value:
        pairs.append(
            (
                f"{prefix}.ElasticInferenceAcceleratorAssociationId",
                str(value["elastic_inference_accelerator_association_id"]),
            )
        )
    if "elastic_inference_accelerator_association_state" in value:
        pairs.append(
            (
                f"{prefix}.ElasticInferenceAcceleratorAssociationState",
                str(value["elastic_inference_accelerator_association_state"]),
            )
        )
    if "elastic_inference_accelerator_association_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["elastic_inference_accelerator_association_time"],
            pairs,
            f"{prefix}.ElasticInferenceAcceleratorAssociationTime",
        )


def deserialize_ec2_query(el: Element) -> ElasticInferenceAcceleratorAssociation:
    out: ElasticInferenceAcceleratorAssociation = {}  # type: ignore[typeddict-item]
    child_elastic_inference_accelerator_arn = el.find("ElasticInferenceAcceleratorArn")
    if child_elastic_inference_accelerator_arn is not None:
        out["elastic_inference_accelerator_arn"] = str(
            child_elastic_inference_accelerator_arn.text or ""
        )
    child_elastic_inference_accelerator_association_id = el.find(
        "ElasticInferenceAcceleratorAssociationId"
    )
    if child_elastic_inference_accelerator_association_id is not None:
        out["elastic_inference_accelerator_association_id"] = str(
            child_elastic_inference_accelerator_association_id.text or ""
        )
    child_elastic_inference_accelerator_association_state = el.find(
        "ElasticInferenceAcceleratorAssociationState"
    )
    if child_elastic_inference_accelerator_association_state is not None:
        out["elastic_inference_accelerator_association_state"] = str(
            child_elastic_inference_accelerator_association_state.text or ""
        )
    child_elastic_inference_accelerator_association_time = el.find(
        "ElasticInferenceAcceleratorAssociationTime"
    )
    if child_elastic_inference_accelerator_association_time is not None:
        import capo_ec2.types.date_time

        out["elastic_inference_accelerator_association_time"] = (
            capo_ec2.types.date_time.deserialize_ec2_query(
                child_elastic_inference_accelerator_association_time
            )
        )
    return out
