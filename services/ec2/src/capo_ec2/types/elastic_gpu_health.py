"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.elastic_gpu_status


class ElasticGpuHealth(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.elastic_gpu_status.ElasticGpuStatus"]
    """<p>The health status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ec2.types.elastic_gpu_status

        capo_ec2.types.elastic_gpu_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_ec2_query(el: Element) -> ElasticGpuHealth:
    out: ElasticGpuHealth = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.elastic_gpu_status

        out["status"] = capo_ec2.types.elastic_gpu_status.deserialize_ec2_query(
            child_status
        )
    return out
