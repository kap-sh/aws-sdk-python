"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeGeneratedTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.generated_template_id
    import capo_cloudformation.types.generated_template_name
    import capo_cloudformation.types.generated_template_status
    import capo_cloudformation.types.last_updated_time
    import capo_cloudformation.types.resource_details
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.template_configuration
    import capo_cloudformation.types.template_progress
    import capo_cloudformation.types.template_status_reason
    import capo_cloudformation.types.total_warnings


class DescribeGeneratedTemplateOutput(TypedDict, closed=True):
    generated_template_id: NotRequired[
        "capo_cloudformation.types.generated_template_id.GeneratedTemplateId"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated template. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}</code>. For example, <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:generatedtemplate/<i>2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc</i> </code>.</p>"""
    generated_template_name: NotRequired[
        "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name of the generated template.</p>"""
    resources: NotRequired["capo_cloudformation.types.resource_details.ResourceDetails"]
    """<p>A list of objects describing the details of the resources in the template generation.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.generated_template_status.GeneratedTemplateStatus"
    ]
    """<p>The status of the template generation. Supported values are:</p> <ul> <li> <p> <code>CreatePending</code> - the creation of the template is pending.</p> </li> <li> <p> <code>CreateInProgress</code> - the creation of the template is in progress.</p> </li> <li> <p> <code>DeletePending</code> - the deletion of the template is pending.</p> </li> <li> <p> <code>DeleteInProgress</code> - the deletion of the template is in progress.</p> </li> <li> <p> <code>UpdatePending</code> - the update of the template is pending.</p> </li> <li> <p> <code>UpdateInProgress</code> - the update of the template is in progress.</p> </li> <li> <p> <code>Failed</code> - the template operation failed.</p> </li> <li> <p> <code>Complete</code> - the template operation is complete.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.template_status_reason.TemplateStatusReason"
    ]
    """<p>The reason for the current template generation status. This will provide more details if a failure happened.</p>"""
    creation_time: NotRequired["capo_cloudformation.types.creation_time.CreationTime"]
    """<p>The time the generated template was created.</p>"""
    last_updated_time: NotRequired[
        "capo_cloudformation.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>The time the generated template was last updated.</p>"""
    progress: NotRequired[
        "capo_cloudformation.types.template_progress.TemplateProgress"
    ]
    """<p>An object describing the progress of the template generation.</p>"""
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The stack ARN of the base stack if a base stack was provided when generating the template.</p>"""
    template_configuration: NotRequired[
        "capo_cloudformation.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The configuration details of the generated template, including the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code>.</p>"""
    total_warnings: NotRequired[
        "capo_cloudformation.types.total_warnings.TotalWarnings"
    ]
    """<p>The number of warnings generated for this template. The warnings are found in the details of each of the resources in the template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGeneratedTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "generated_template_id" in value:
        pairs.append(
            (f"{key_prefix}GeneratedTemplateId", str(value["generated_template_id"]))
        )
    if "generated_template_name" in value:
        pairs.append(
            (
                f"{key_prefix}GeneratedTemplateName",
                str(value["generated_template_name"]),
            )
        )
    if "resources" in value:
        import capo_cloudformation.types.resource_details

        capo_cloudformation.types.resource_details.serialize_query(
            value["resources"], pairs, f"{key_prefix}Resources"
        )
    if "status" in value:
        import capo_cloudformation.types.generated_template_status

        capo_cloudformation.types.generated_template_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "creation_time" in value:
        import capo_cloudformation.types.creation_time

        capo_cloudformation.types.creation_time.serialize_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "last_updated_time" in value:
        import capo_cloudformation.types.last_updated_time

        capo_cloudformation.types.last_updated_time.serialize_query(
            value["last_updated_time"], pairs, f"{key_prefix}LastUpdatedTime"
        )
    if "progress" in value:
        import capo_cloudformation.types.template_progress

        capo_cloudformation.types.template_progress.serialize_query(
            value["progress"], pairs, f"{key_prefix}Progress"
        )
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "template_configuration" in value:
        import capo_cloudformation.types.template_configuration

        capo_cloudformation.types.template_configuration.serialize_query(
            value["template_configuration"], pairs, f"{key_prefix}TemplateConfiguration"
        )
    if "total_warnings" in value:
        pairs.append((f"{key_prefix}TotalWarnings", str(value["total_warnings"])))


def deserialize_query(el: Element) -> DescribeGeneratedTemplateOutput:
    out: DescribeGeneratedTemplateOutput = {}  # type: ignore[typeddict-item]
    child_generated_template_id = el.find("GeneratedTemplateId")
    if child_generated_template_id is not None:
        out["generated_template_id"] = str(child_generated_template_id.text or "")
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
    child_resources = el.find("Resources")
    if child_resources is not None:
        import capo_cloudformation.types.resource_details

        out["resources"] = capo_cloudformation.types.resource_details.deserialize_query(
            child_resources
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.generated_template_status

        out["status"] = (
            capo_cloudformation.types.generated_template_status.deserialize_query(
                child_status
            )
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_cloudformation.types.creation_time

        out["creation_time"] = (
            capo_cloudformation.types.creation_time.deserialize_query(
                child_creation_time
            )
        )
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        import capo_cloudformation.types.last_updated_time

        out["last_updated_time"] = (
            capo_cloudformation.types.last_updated_time.deserialize_query(
                child_last_updated_time
            )
        )
    child_progress = el.find("Progress")
    if child_progress is not None:
        import capo_cloudformation.types.template_progress

        out["progress"] = capo_cloudformation.types.template_progress.deserialize_query(
            child_progress
        )
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_template_configuration = el.find("TemplateConfiguration")
    if child_template_configuration is not None:
        import capo_cloudformation.types.template_configuration

        out["template_configuration"] = (
            capo_cloudformation.types.template_configuration.deserialize_query(
                child_template_configuration
            )
        )
    child_total_warnings = el.find("TotalWarnings")
    if child_total_warnings is not None:
        out["total_warnings"] = int(child_total_warnings.text or "")
    return out
