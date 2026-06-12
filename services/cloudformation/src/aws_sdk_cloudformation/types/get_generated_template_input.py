"""Generated from Smithy shape ``com.amazonaws.cloudformation#GetGeneratedTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.generated_template_name
    import aws_sdk_cloudformation.types.template_format


class GetGeneratedTemplateInput(TypedDict):
    format: NotRequired["aws_sdk_cloudformation.types.template_format.TemplateFormat"]
    """<p>The language to use to retrieve for the generated template. Supported values are:</p> <ul> <li> <p> <code>JSON</code> </p> </li> <li> <p> <code>YAML</code> </p> </li> </ul>"""
    generated_template_name: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the generated template. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}</code>. For example, <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:generatedtemplate/<i>2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc</i> </code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetGeneratedTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "format" in value:
        import aws_sdk_cloudformation.types.template_format

        aws_sdk_cloudformation.types.template_format.serialize_query(
            value["format"], pairs, f"{prefix}.Format"
        )
    if "generated_template_name" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateName", str(value["generated_template_name"]))
        )


def deserialize_query(el: Element) -> GetGeneratedTemplateInput:
    out: GetGeneratedTemplateInput = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_cloudformation.types.template_format

        out["format"] = aws_sdk_cloudformation.types.template_format.deserialize_query(
            child_format
        )
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
    return out
