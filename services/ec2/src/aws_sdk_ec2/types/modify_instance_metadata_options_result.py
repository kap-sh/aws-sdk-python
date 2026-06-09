"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_metadata_options_response
    import aws_sdk_ec2.types.string


class ModifyInstanceMetadataOptionsResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_metadata_options: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_options_response.InstanceMetadataOptionsResponse"
    ]
    """<p>The metadata options for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceMetadataOptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_metadata_options" in value:
        import aws_sdk_ec2.types.instance_metadata_options_response

        aws_sdk_ec2.types.instance_metadata_options_response.serialize_ec2_query(
            value["instance_metadata_options"],
            pairs,
            f"{prefix}.InstanceMetadataOptions",
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceMetadataOptionsResult:
    out: ModifyInstanceMetadataOptionsResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_metadata_options = el.find("InstanceMetadataOptions")
    if child_instance_metadata_options is not None:
        import aws_sdk_ec2.types.instance_metadata_options_response

        out["instance_metadata_options"] = (
            aws_sdk_ec2.types.instance_metadata_options_response.deserialize_ec2_query(
                child_instance_metadata_options
            )
        )
    return out
