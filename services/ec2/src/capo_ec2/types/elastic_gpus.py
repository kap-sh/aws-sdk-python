"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpu_health
    import capo_ec2.types.elastic_gpu_state
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ElasticGpus(TypedDict, closed=True):
    elastic_gpu_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Elastic Graphics accelerator.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in the which the Elastic Graphics accelerator resides.</p>"""
    elastic_gpu_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of Elastic Graphics accelerator.</p>"""
    elastic_gpu_health: NotRequired[
        "capo_ec2.types.elastic_gpu_health.ElasticGpuHealth"
    ]
    """<p>The status of the Elastic Graphics accelerator.</p>"""
    elastic_gpu_state: NotRequired["capo_ec2.types.elastic_gpu_state.ElasticGpuState"]
    """<p>The state of the Elastic Graphics accelerator.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance to which the Elastic Graphics accelerator is attached.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Elastic Graphics accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "elastic_gpu_id" in value:
        pairs.append((f"{key_prefix}ElasticGpuId", str(value["elastic_gpu_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "elastic_gpu_type" in value:
        pairs.append((f"{key_prefix}ElasticGpuType", str(value["elastic_gpu_type"])))
    if "elastic_gpu_health" in value:
        import capo_ec2.types.elastic_gpu_health

        capo_ec2.types.elastic_gpu_health.serialize_ec2_query(
            value["elastic_gpu_health"], pairs, f"{key_prefix}ElasticGpuHealth"
        )
    if "elastic_gpu_state" in value:
        import capo_ec2.types.elastic_gpu_state

        capo_ec2.types.elastic_gpu_state.serialize_ec2_query(
            value["elastic_gpu_state"], pairs, f"{key_prefix}ElasticGpuState"
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> ElasticGpus:
    out: ElasticGpus = {}  # type: ignore[typeddict-item]
    child_elastic_gpu_id = el.find("elasticGpuId")
    if child_elastic_gpu_id is not None:
        out["elastic_gpu_id"] = str(child_elastic_gpu_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_elastic_gpu_type = el.find("elasticGpuType")
    if child_elastic_gpu_type is not None:
        out["elastic_gpu_type"] = str(child_elastic_gpu_type.text or "")
    child_elastic_gpu_health = el.find("elasticGpuHealth")
    if child_elastic_gpu_health is not None:
        import capo_ec2.types.elastic_gpu_health

        out["elastic_gpu_health"] = (
            capo_ec2.types.elastic_gpu_health.deserialize_ec2_query(
                child_elastic_gpu_health
            )
        )
    child_elastic_gpu_state = el.find("elasticGpuState")
    if child_elastic_gpu_state is not None:
        import capo_ec2.types.elastic_gpu_state

        out["elastic_gpu_state"] = (
            capo_ec2.types.elastic_gpu_state.deserialize_ec2_query(
                child_elastic_gpu_state
            )
        )
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
