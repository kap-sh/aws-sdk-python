"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_environment
    import capo_ec2.types.export_to_s3_task_specification
    import capo_ec2.types.instance_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateInstanceExportTaskRequest(TypedDict, closed=True):
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the export instance task during creation.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the conversion task or the resource being exported. The maximum length is 255 characters.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    target_environment: NotRequired[
        "capo_ec2.types.export_environment.ExportEnvironment"
    ]
    """<p>The target virtualization environment.</p>"""
    export_to_s3_task: NotRequired[
        "capo_ec2.types.export_to_s3_task_specification.ExportToS3TaskSpecification"
    ]
    """<p>The format and location for an export instance task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceExportTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "target_environment" in value:
        import capo_ec2.types.export_environment

        capo_ec2.types.export_environment.serialize_ec2_query(
            value["target_environment"], pairs, f"{prefix}.TargetEnvironment"
        )
    if "export_to_s3_task" in value:
        import capo_ec2.types.export_to_s3_task_specification

        capo_ec2.types.export_to_s3_task_specification.serialize_ec2_query(
            value["export_to_s3_task"], pairs, f"{prefix}.ExportToS3"
        )


def deserialize_ec2_query(el: Element) -> CreateInstanceExportTaskRequest:
    out: CreateInstanceExportTaskRequest = {}  # type: ignore[typeddict-item]
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_target_environment = el.find("TargetEnvironment")
    if child_target_environment is not None:
        import capo_ec2.types.export_environment

        out["target_environment"] = (
            capo_ec2.types.export_environment.deserialize_ec2_query(
                child_target_environment
            )
        )
    child_export_to_s3_task = el.find("ExportToS3")
    if child_export_to_s3_task is not None:
        import capo_ec2.types.export_to_s3_task_specification

        out["export_to_s3_task"] = (
            capo_ec2.types.export_to_s3_task_specification.deserialize_ec2_query(
                child_export_to_s3_task
            )
        )
    return out
