"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.description
    import aws_sdk_cloudformation.types.no_echo
    import aws_sdk_cloudformation.types.parameter_key
    import aws_sdk_cloudformation.types.parameter_value


class TemplateParameter(TypedDict, closed=True):
    parameter_key: NotRequired[
        "aws_sdk_cloudformation.types.parameter_key.ParameterKey"
    ]
    """<p>The name associated with the parameter.</p>"""
    default_value: NotRequired[
        "aws_sdk_cloudformation.types.parameter_value.ParameterValue"
    ]
    """<p>The default value associated with the parameter.</p>"""
    no_echo: NotRequired["aws_sdk_cloudformation.types.no_echo.NoEcho"]
    """<p>Flag indicating whether the parameter should be displayed as plain text in logs and UIs.</p>"""
    description: NotRequired["aws_sdk_cloudformation.types.description.Description"]
    """<p>User defined description associated with the parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateParameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_key" in value:
        pairs.append((f"{prefix}.ParameterKey", str(value["parameter_key"])))
    if "default_value" in value:
        pairs.append((f"{prefix}.DefaultValue", str(value["default_value"])))
    if "no_echo" in value:
        pairs.append((f"{prefix}.NoEcho", "true" if value["no_echo"] else "false"))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> TemplateParameter:
    out: TemplateParameter = {}  # type: ignore[typeddict-item]
    child_parameter_key = el.find("ParameterKey")
    if child_parameter_key is not None:
        out["parameter_key"] = str(child_parameter_key.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_no_echo = el.find("NoEcho")
    if child_no_echo is not None:
        out["no_echo"] = (child_no_echo.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
