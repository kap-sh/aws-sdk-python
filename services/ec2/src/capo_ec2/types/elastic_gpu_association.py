"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpu_id
    import capo_ec2.types.string


class ElasticGpuAssociation(TypedDict, closed=True):
    elastic_gpu_id: NotRequired["capo_ec2.types.elastic_gpu_id.ElasticGpuId"]
    """<p>The ID of the Elastic Graphics accelerator.</p>"""
    elastic_gpu_association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    elastic_gpu_association_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state of the association between the instance and the Elastic Graphics accelerator.</p>"""
    elastic_gpu_association_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The time the Elastic Graphics accelerator was associated with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "elastic_gpu_id" in value:
        pairs.append((f"{key_prefix}ElasticGpuId", str(value["elastic_gpu_id"])))
    if "elastic_gpu_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}ElasticGpuAssociationId",
                str(value["elastic_gpu_association_id"]),
            )
        )
    if "elastic_gpu_association_state" in value:
        pairs.append(
            (
                f"{key_prefix}ElasticGpuAssociationState",
                str(value["elastic_gpu_association_state"]),
            )
        )
    if "elastic_gpu_association_time" in value:
        pairs.append(
            (
                f"{key_prefix}ElasticGpuAssociationTime",
                str(value["elastic_gpu_association_time"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ElasticGpuAssociation:
    out: ElasticGpuAssociation = {}  # type: ignore[typeddict-item]
    child_elastic_gpu_id = el.find("ElasticGpuId")
    if child_elastic_gpu_id is not None:
        out["elastic_gpu_id"] = str(child_elastic_gpu_id.text or "")
    child_elastic_gpu_association_id = el.find("ElasticGpuAssociationId")
    if child_elastic_gpu_association_id is not None:
        out["elastic_gpu_association_id"] = str(
            child_elastic_gpu_association_id.text or ""
        )
    child_elastic_gpu_association_state = el.find("ElasticGpuAssociationState")
    if child_elastic_gpu_association_state is not None:
        out["elastic_gpu_association_state"] = str(
            child_elastic_gpu_association_state.text or ""
        )
    child_elastic_gpu_association_time = el.find("ElasticGpuAssociationTime")
    if child_elastic_gpu_association_time is not None:
        out["elastic_gpu_association_time"] = str(
            child_elastic_gpu_association_time.text or ""
        )
    return out
