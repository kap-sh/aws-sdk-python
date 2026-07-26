"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCpuOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id
    import capo_ec2.types.integer
    import capo_ec2.types.nested_virtualization_specification


class ModifyInstanceCpuOptionsResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance that was updated.</p>"""
    core_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of CPU cores that are running for the specified instance after the update.</p>"""
    threads_per_core: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of threads that are running per CPU core for the specified instance after the update.</p>"""
    nested_virtualization: NotRequired[
        "capo_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether nested virtualization has been enabled or disabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCpuOptionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "core_count" in value:
        pairs.append((f"{prefix}.CoreCount", str(value["core_count"])))
    if "threads_per_core" in value:
        pairs.append((f"{prefix}.ThreadsPerCore", str(value["threads_per_core"])))
    if "nested_virtualization" in value:
        import capo_ec2.types.nested_virtualization_specification

        capo_ec2.types.nested_virtualization_specification.serialize_ec2_query(
            value["nested_virtualization"], pairs, f"{prefix}.NestedVirtualization"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceCpuOptionsResult:
    out: ModifyInstanceCpuOptionsResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_core_count = el.find("CoreCount")
    if child_core_count is not None:
        out["core_count"] = int(child_core_count.text or "")
    child_threads_per_core = el.find("ThreadsPerCore")
    if child_threads_per_core is not None:
        out["threads_per_core"] = int(child_threads_per_core.text or "")
    child_nested_virtualization = el.find("NestedVirtualization")
    if child_nested_virtualization is not None:
        import capo_ec2.types.nested_virtualization_specification

        out["nested_virtualization"] = (
            capo_ec2.types.nested_virtualization_specification.deserialize_ec2_query(
                child_nested_virtualization
            )
        )
    return out
