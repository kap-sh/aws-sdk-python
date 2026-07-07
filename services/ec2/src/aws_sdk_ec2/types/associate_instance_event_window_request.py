"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_event_window_association_request
    import aws_sdk_ec2.types.instance_event_window_id


class AssociateInstanceEventWindowRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    association_target: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_association_request.InstanceEventWindowAssociationRequest"
    ]
    """<p>One or more targets associated with the specified event window.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateInstanceEventWindowRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "instance_event_window_id" in value:
        pairs.append(
            (f"{prefix}.InstanceEventWindowId", str(value["instance_event_window_id"]))
        )
    if "association_target" in value:
        import aws_sdk_ec2.types.instance_event_window_association_request

        aws_sdk_ec2.types.instance_event_window_association_request.serialize_ec2_query(
            value["association_target"], pairs, f"{prefix}.AssociationTarget"
        )


def deserialize_ec2_query(el: Element) -> AssociateInstanceEventWindowRequest:
    out: AssociateInstanceEventWindowRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_event_window_id = el.find("InstanceEventWindowId")
    if child_instance_event_window_id is not None:
        out["instance_event_window_id"] = str(child_instance_event_window_id.text or "")
    child_association_target = el.find("AssociationTarget")
    if child_association_target is not None:
        import aws_sdk_ec2.types.instance_event_window_association_request

        out["association_target"] = (
            aws_sdk_ec2.types.instance_event_window_association_request.deserialize_ec2_query(
                child_association_target
            )
        )
    return out
