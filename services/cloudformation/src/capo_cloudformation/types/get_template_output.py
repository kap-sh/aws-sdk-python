"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.stage_list
    import capo_cloudformation.types.template_body


class GetTemplateOutput(TypedDict, closed=True):
    template_body: NotRequired["capo_cloudformation.types.template_body.TemplateBody"]
    """<p>Structure that contains the template body.</p> <p>CloudFormation returns the same template that was used when the stack was created.</p>"""
    stages_available: NotRequired["capo_cloudformation.types.stage_list.StageList"]
    """<p>The stage of the template that you can retrieve. For stacks, the <code>Original</code> and <code>Processed</code> templates are always available. For change sets, the <code>Original</code> template is always available. After CloudFormation finishes creating the change set, the <code>Processed</code> template becomes available.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "template_body" in value:
        pairs.append((f"{prefix}.TemplateBody", str(value["template_body"])))
    if "stages_available" in value:
        import capo_cloudformation.types.stage_list

        capo_cloudformation.types.stage_list.serialize_query(
            value["stages_available"], pairs, f"{prefix}.StagesAvailable"
        )


def deserialize_query(el: Element) -> GetTemplateOutput:
    out: GetTemplateOutput = {}  # type: ignore[typeddict-item]
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_stages_available = el.find("StagesAvailable")
    if child_stages_available is not None:
        import capo_cloudformation.types.stage_list

        out["stages_available"] = (
            capo_cloudformation.types.stage_list.deserialize_query(
                child_stages_available
            )
        )
    return out
