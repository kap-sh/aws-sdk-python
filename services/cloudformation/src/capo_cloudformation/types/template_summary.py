"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.generated_template_id
    import capo_cloudformation.types.generated_template_name
    import capo_cloudformation.types.generated_template_status
    import capo_cloudformation.types.last_updated_time
    import capo_cloudformation.types.number_of_resources
    import capo_cloudformation.types.template_status_reason


class TemplateSummary(TypedDict, closed=True):
    generated_template_id: NotRequired[
        "capo_cloudformation.types.generated_template_id.GeneratedTemplateId"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated template. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}</code>. For example, <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:generatedtemplate/<i>2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc</i> </code>.</p>"""
    generated_template_name: NotRequired[
        "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name of the generated template.</p>"""
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
    number_of_resources: NotRequired[
        "capo_cloudformation.types.number_of_resources.NumberOfResources"
    ]
    """<p>The number of resources in the generated template. This is a total of resources in pending, in-progress, completed, and failed states.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "generated_template_id" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateId", str(value["generated_template_id"]))
        )
    if "generated_template_name" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateName", str(value["generated_template_name"]))
        )
    if "status" in value:
        import capo_cloudformation.types.generated_template_status

        capo_cloudformation.types.generated_template_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_reason" in value:
        pairs.append((f"{prefix}.StatusReason", str(value["status_reason"])))
    if "creation_time" in value:
        import capo_cloudformation.types.creation_time

        capo_cloudformation.types.creation_time.serialize_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "last_updated_time" in value:
        import capo_cloudformation.types.last_updated_time

        capo_cloudformation.types.last_updated_time.serialize_query(
            value["last_updated_time"], pairs, f"{prefix}.LastUpdatedTime"
        )
    if "number_of_resources" in value:
        pairs.append((f"{prefix}.NumberOfResources", str(value["number_of_resources"])))


def deserialize_query(el: Element) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    child_generated_template_id = el.find("GeneratedTemplateId")
    if child_generated_template_id is not None:
        out["generated_template_id"] = str(child_generated_template_id.text or "")
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
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
    child_number_of_resources = el.find("NumberOfResources")
    if child_number_of_resources is not None:
        out["number_of_resources"] = int(child_number_of_resources.text or "")
    return out
