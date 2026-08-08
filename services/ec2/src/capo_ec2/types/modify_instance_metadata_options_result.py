"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_metadata_options_response
    import capo_ec2.types.string


class ModifyInstanceMetadataOptionsResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_metadata_options: NotRequired[
        "capo_ec2.types.instance_metadata_options_response.InstanceMetadataOptionsResponse"
    ]
    """<p>The metadata options for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceMetadataOptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_metadata_options" in value:
        import capo_ec2.types.instance_metadata_options_response

        capo_ec2.types.instance_metadata_options_response.serialize_ec2_query(
            value["instance_metadata_options"],
            pairs,
            f"{key_prefix}InstanceMetadataOptions",
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceMetadataOptionsResult:
    out: ModifyInstanceMetadataOptionsResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_metadata_options = el.find("instanceMetadataOptions")
    if child_instance_metadata_options is not None:
        import capo_ec2.types.instance_metadata_options_response

        out["instance_metadata_options"] = (
            capo_ec2.types.instance_metadata_options_response.deserialize_ec2_query(
                child_instance_metadata_options
            )
        )
    return out
