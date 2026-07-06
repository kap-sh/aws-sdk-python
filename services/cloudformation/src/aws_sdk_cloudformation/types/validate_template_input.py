"""Generated from Smithy shape ``com.amazonaws.cloudformation#ValidateTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.template_body
    import aws_sdk_cloudformation.types.template_url


class ValidateTemplateInput(TypedDict, closed=True):
    template_body: NotRequired[
        "aws_sdk_cloudformation.types.template_body.TemplateBody"
    ]
    """<p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>"""
    template_url: NotRequired["aws_sdk_cloudformation.types.template_url.TemplateURL"]
    """<p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidateTemplateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "template_body" in value:
        pairs.append((f"{prefix}.TemplateBody", str(value["template_body"])))
    if "template_url" in value:
        pairs.append((f"{prefix}.TemplateURL", str(value["template_url"])))


def deserialize_query(el: Element) -> ValidateTemplateInput:
    out: ValidateTemplateInput = {}  # type: ignore[typeddict-item]
    child_template_body = el.find("TemplateBody")
    if child_template_body is not None:
        out["template_body"] = str(child_template_body.text or "")
    child_template_url = el.find("TemplateURL")
    if child_template_url is not None:
        out["template_url"] = str(child_template_url.text or "")
    return out
