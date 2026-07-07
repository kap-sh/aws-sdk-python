"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreateGeneratedTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.generated_template_id


class CreateGeneratedTemplateOutput(TypedDict, closed=True):
    generated_template_id: NotRequired[
        "aws_sdk_cloudformation.types.generated_template_id.GeneratedTemplateId"
    ]
    """<p>The ID of the generated template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGeneratedTemplateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "generated_template_id" in value:
        pairs.append(
            (f"{prefix}.GeneratedTemplateId", str(value["generated_template_id"]))
        )


def deserialize_query(el: Element) -> CreateGeneratedTemplateOutput:
    out: CreateGeneratedTemplateOutput = {}  # type: ignore[typeddict-item]
    child_generated_template_id = el.find("GeneratedTemplateId")
    if child_generated_template_id is not None:
        out["generated_template_id"] = str(child_generated_template_id.text or "")
    return out
