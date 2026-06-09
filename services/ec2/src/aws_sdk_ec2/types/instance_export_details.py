"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceExportDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_environment
    import aws_sdk_ec2.types.string


class InstanceExportDetails(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource being exported.</p>"""
    target_environment: NotRequired[
        "aws_sdk_ec2.types.export_environment.ExportEnvironment"
    ]
    """<p>The target virtualization environment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceExportDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "target_environment" in value:
        import aws_sdk_ec2.types.export_environment

        aws_sdk_ec2.types.export_environment.serialize_ec2_query(
            value["target_environment"], pairs, f"{prefix}.TargetEnvironment"
        )


def deserialize_ec2_query(el: Element) -> InstanceExportDetails:
    out: InstanceExportDetails = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_target_environment = el.find("TargetEnvironment")
    if child_target_environment is not None:
        import aws_sdk_ec2.types.export_environment

        out["target_environment"] = (
            aws_sdk_ec2.types.export_environment.deserialize_ec2_query(
                child_target_environment
            )
        )
    return out
