"""Generated from Smithy shape ``com.amazonaws.iam#SourceRoleTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.integer_type


class SourceRoleTemplate(TypedDict, closed=True):
    template_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the role template that the role was created from.</p>"""
    template_minor_version: "capo_iam.types.integer_type.integerType"
    """<p>The minor version of the role template that was used to create the role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceRoleTemplate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateArn", str(value["template_arn"])))
    pairs.append(
        (f"{key_prefix}TemplateMinorVersion", str(value["template_minor_version"]))
    )


def deserialize_query(el: Element) -> SourceRoleTemplate:
    out: SourceRoleTemplate = {}  # type: ignore[typeddict-item]
    child_template_arn = el.find("TemplateArn")
    if child_template_arn is not None:
        out["template_arn"] = str(child_template_arn.text or "")
    else:
        raise DeserializationError("SourceRoleTemplate.template_arn required")
    child_template_minor_version = el.find("TemplateMinorVersion")
    if child_template_minor_version is not None:
        out["template_minor_version"] = int(child_template_minor_version.text or "")
    else:
        raise DeserializationError("SourceRoleTemplate.template_minor_version required")
    return out
