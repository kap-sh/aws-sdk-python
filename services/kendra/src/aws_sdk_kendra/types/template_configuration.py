"""Generated from Smithy shape ``com.amazonaws.kendra#TemplateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.template


class TemplateConfiguration(TypedDict):
    template: NotRequired["aws_sdk_kendra.types.template.Template"]
    r"""<p>The template schema used for the data source, where templates schemas are supported.</p> <p>See <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html\">Data source template schemas</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TemplateConfiguration) -> dict:
    out: dict = {}
    if "template" in value:
        out["Template"] = value["template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TemplateConfiguration:
    out: TemplateConfiguration = {}  # type: ignore[typeddict-item]
    if "Template" in data:
        out["template"] = data["Template"]
    return out
