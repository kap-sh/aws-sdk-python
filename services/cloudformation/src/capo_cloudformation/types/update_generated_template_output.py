"""Generated from Smithy shape ``com.amazonaws.cloudformation#UpdateGeneratedTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.generated_template_id


class UpdateGeneratedTemplateOutput(TypedDict, closed=True):
    generated_template_id: NotRequired[
        "capo_cloudformation.types.generated_template_id.GeneratedTemplateId"
    ]
    """<p>The Amazon Resource Name (ARN) of the generated template. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}</code>. For example, <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:generatedtemplate/<i>2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc</i> </code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateGeneratedTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "generated_template_id" in value:
        pairs.append(
            (f"{key_prefix}GeneratedTemplateId", str(value["generated_template_id"]))
        )


def deserialize_query(el: Element) -> UpdateGeneratedTemplateOutput:
    out: UpdateGeneratedTemplateOutput = {}  # type: ignore[typeddict-item]
    child_generated_template_id = el.find("GeneratedTemplateId")
    if child_generated_template_id is not None:
        out["generated_template_id"] = str(child_generated_template_id.text or "")
    return out
