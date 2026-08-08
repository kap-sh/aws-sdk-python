"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.boolean
    import capo_ec2.types.volume_id


class ModifyVolumeAttributeRequest(TypedDict, closed=True):
    auto_enable_io: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the volume should be auto-enabled for I/O operations.</p>"""
    volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVolumeAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_enable_io" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["auto_enable_io"], pairs, f"{key_prefix}AutoEnableIO"
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVolumeAttributeRequest:
    out: ModifyVolumeAttributeRequest = {}  # type: ignore[typeddict-item]
    child_auto_enable_io = el.find("AutoEnableIO")
    if child_auto_enable_io is not None:
        import capo_ec2.types.attribute_boolean_value

        out["auto_enable_io"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_auto_enable_io
            )
        )
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
