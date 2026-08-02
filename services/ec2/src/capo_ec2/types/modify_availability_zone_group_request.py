"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAvailabilityZoneGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.modify_availability_zone_opt_in_status
    import capo_ec2.types.string


class ModifyAvailabilityZoneGroupRequest(TypedDict, closed=True):
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Availability Zone group, Local Zone group, or Wavelength Zone group.</p>"""
    opt_in_status: NotRequired[
        "capo_ec2.types.modify_availability_zone_opt_in_status.ModifyAvailabilityZoneOptInStatus"
    ]
    """<p>Indicates whether to opt in to the zone group. The only valid value is <code>opted-in</code>. You must contact Amazon Web Services Support to opt out of a Local Zone or Wavelength Zone group.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyAvailabilityZoneGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "opt_in_status" in value:
        import capo_ec2.types.modify_availability_zone_opt_in_status

        capo_ec2.types.modify_availability_zone_opt_in_status.serialize_ec2_query(
            value["opt_in_status"], pairs, f"{key_prefix}OptInStatus"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyAvailabilityZoneGroupRequest:
    out: ModifyAvailabilityZoneGroupRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_opt_in_status = el.find("OptInStatus")
    if child_opt_in_status is not None:
        import capo_ec2.types.modify_availability_zone_opt_in_status

        out["opt_in_status"] = (
            capo_ec2.types.modify_availability_zone_opt_in_status.deserialize_ec2_query(
                child_opt_in_status
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
