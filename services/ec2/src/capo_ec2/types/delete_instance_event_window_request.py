"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_event_window_id


class DeleteInstanceEventWindowRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    force_delete: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> to force delete the event window. Use the force delete parameter if the event window is currently associated with targets.</p>"""
    instance_event_window_id: NotRequired[
        "capo_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteInstanceEventWindowRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "force_delete" in value:
        pairs.append(
            (f"{prefix}.ForceDelete", "true" if value["force_delete"] else "false")
        )
    if "instance_event_window_id" in value:
        pairs.append(
            (f"{prefix}.InstanceEventWindowId", str(value["instance_event_window_id"]))
        )


def deserialize_ec2_query(el: Element) -> DeleteInstanceEventWindowRequest:
    out: DeleteInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_force_delete = el.find("ForceDelete")
    if child_force_delete is not None:
        out["force_delete"] = (child_force_delete.text or "").lower() == "true"
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    return out
