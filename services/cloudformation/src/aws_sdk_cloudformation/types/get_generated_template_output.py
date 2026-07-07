"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetGeneratedTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.generated_template_status
    import aws_sdk_cloudformation.types.template_body


class GetGeneratedTemplateOutput(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_status.GeneratedTemplateStatus"
    ]
    """<p>The status of the template generation. Supported values are:</p> <ul> <li> <p> <code>CreatePending</code> - the creation of the template is pending.</p> </li> <li> <p> <code>CreateInProgress</code> - the creation of the template is in progress.</p> </li> <li> <p> <code>DeletePending</code> - the deletion of the template is pending.</p> </li> <li> <p> <code>DeleteInProgress</code> - the deletion of the template is in progress.</p> </li> <li> <p> <code>UpdatePending</code> - the update of the template is pending.</p> </li> <li> <p> <code>UpdateInProgress</code> - the update of the template is in progress.</p> </li> <li> <p> <code>Failed</code> - the template operation failed.</p> </li> <li> <p> <code>Complete</code> - the template operation is complete.</p> </li> </ul>"""
    template_body: NotRequired[
        "aws_sdk_cloudformation.types.template_body.TemplateBody"
    ]
    """<p>The template body of the generated template, in the language specified by the <code>Language</code> parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetGeneratedTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_cloudformation.types.generated_template_status

        aws_sdk_cloudformation.types.generated_template_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "template_body" in value:
        pairs.append((f"{prefix}.TemplateBody", str(value["template_body"])))


def deserialize_query(el: Element) -> GetGeneratedTemplateOutput:
    out: GetGeneratedTemplateOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudformation.types.generated_template_status

        out["status"] = (
            aws_sdk_cloudformation.types.generated_template_status.deserialize_query(
                child_status
            )
        )
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    return out
