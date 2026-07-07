"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeGeneratedTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.generated_template_name


class DescribeGeneratedTemplateInput(TypedDict, closed=True):
    generated_template_name: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_name.GeneratedTemplateName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of a generated template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeGeneratedTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "generated_template_name" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateName", str(value["generated_template_name"]))
        )


def deserialize_query(el: Element) -> DescribeGeneratedTemplateInput:
    out: DescribeGeneratedTemplateInput = {}  # type: ignore[typeddict-item]
    child_generated_template_name = el.find("GeneratedTemplateName")
    if child_generated_template_name is not None:
        out["generated_template_name"] = str(child_generated_template_name.text or "")
    return out
