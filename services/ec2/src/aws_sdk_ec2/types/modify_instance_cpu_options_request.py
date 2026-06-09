"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCpuOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class ModifyInstanceCpuOptionsRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to update.</p>"""
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores to activate for the specified instance.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads to run for each CPU core.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether to enable or disable nested virtualization for the instance. When nested virtualization is enabled, Virtual Secure Mode (VSM) is automatically disabled for the instance.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceCpuOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "core_count" in value:
        pairs.append((f"{prefix}.CoreCount", str(value["core_count"])))
    if "threads_per_core" in value:
        pairs.append((f"{prefix}.ThreadsPerCore", str(value["threads_per_core"])))
    if "nested_virtualization" in value:
        import aws_sdk_ec2.types.nested_virtualization_specification

        aws_sdk_ec2.types.nested_virtualization_specification.serialize_ec2_query(
            value["nested_virtualization"], pairs, f"{prefix}.NestedVirtualization"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyInstanceCpuOptionsRequest:
    out: ModifyInstanceCpuOptionsRequest = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_ec2.types.nested_virtualization_specification

        out["nested_virtualization"] = (
            aws_sdk_ec2.types.nested_virtualization_specification.deserialize_ec2_query(
                child_nested_virtualization
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
