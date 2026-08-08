"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id_string_list


class TerminateInstancesRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the instances.</p> <p>Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.</p>"""
    force: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Forces the instances to terminate. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.</p>"""
    skip_os_shutdown: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to bypass the graceful OS shutdown process when the instance is terminated.</p> <p>Default: <code>false</code> </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "force" in value:
        pairs.append((f"{key_prefix}Force", "true" if value["force"] else "false"))
    if "skip_os_shutdown" in value:
        pairs.append(
            (
                f"{key_prefix}SkipOsShutdown",
                "true" if value["skip_os_shutdown"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> TerminateInstancesRequest:
    out: TerminateInstancesRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceId") is not None:
        import capo_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceId"
            )
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_skip_os_shutdown = el.find("SkipOsShutdown")
    if child_skip_os_shutdown is not None:
        out["skip_os_shutdown"] = (child_skip_os_shutdown.text or "").lower() == "true"
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
