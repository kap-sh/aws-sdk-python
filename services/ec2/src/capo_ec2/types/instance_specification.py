"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_id_with_volume_resolver
    import capo_ec2.types.volume_id_string_list


class InstanceSpecification(TypedDict, closed=True):
    instance_id: NotRequired[
        "capo_ec2.types.instance_id_with_volume_resolver.InstanceIdWithVolumeResolver"
    ]
    """<p>The instance to specify which volumes should be snapshotted.</p>"""
    exclude_boot_volume: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Excludes the root volume from being snapshotted.</p>"""
    exclude_data_volume_ids: NotRequired[
        "capo_ec2.types.volume_id_string_list.VolumeIdStringList"
    ]
    """<p>The IDs of the data (non-root) volumes to exclude from the multi-volume snapshot set. If you specify the ID of the root volume, the request fails. To exclude the root volume, use <b>ExcludeBootVolume</b>.</p> <p>You can specify up to 40 volume IDs per request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "exclude_boot_volume" in value:
        pairs.append(
            (
                f"{key_prefix}ExcludeBootVolume",
                "true" if value["exclude_boot_volume"] else "false",
            )
        )
    if "exclude_data_volume_ids" in value:
        import capo_ec2.types.volume_id_string_list

        capo_ec2.types.volume_id_string_list.serialize_ec2_query(
            value["exclude_data_volume_ids"], pairs, f"{key_prefix}ExcludeDataVolumeId"
        )


def deserialize_ec2_query(el: Element) -> InstanceSpecification:
    out: InstanceSpecification = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_exclude_boot_volume = el.find("ExcludeBootVolume")
    if child_exclude_boot_volume is not None:
        out["exclude_boot_volume"] = (
            child_exclude_boot_volume.text or ""
        ).lower() == "true"
    child_exclude_data_volume_ids = el.find("ExcludeDataVolumeId")
    if child_exclude_data_volume_ids is not None:
        import capo_ec2.types.volume_id_string_list

        out["exclude_data_volume_ids"] = (
            capo_ec2.types.volume_id_string_list.deserialize_ec2_query(
                child_exclude_data_volume_ids
            )
        )
    return out
