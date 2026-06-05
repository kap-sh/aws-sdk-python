"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceTaskDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_instance_volume_detail_set
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.string


class ImportInstanceTaskDetails(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the task.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""
    volumes: NotRequired[
        "aws_sdk_ec2.types.import_instance_volume_detail_set.ImportInstanceVolumeDetailSet"
    ]
    """<p>The volumes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceTaskDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "platform" in value:
        import aws_sdk_ec2.types.platform_values

        aws_sdk_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{prefix}.Platform"
        )
    if "volumes" in value:
        import aws_sdk_ec2.types.import_instance_volume_detail_set

        aws_sdk_ec2.types.import_instance_volume_detail_set.serialize_ec2_query(
            value["volumes"], pairs, f"{prefix}.Volumes"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceTaskDetails:
    out: ImportInstanceTaskDetails = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        import aws_sdk_ec2.types.platform_values

        out["platform"] = aws_sdk_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    if el.find("Volumes") is not None:
        import aws_sdk_ec2.types.import_instance_volume_detail_set

        out["volumes"] = (
            aws_sdk_ec2.types.import_instance_volume_detail_set.deserialize_ec2_query(
                el, "Volumes"
            )
        )
    return out
