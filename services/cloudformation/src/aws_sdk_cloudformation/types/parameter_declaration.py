"""Generated from Smithy shape ``com.amazonaws.cloudformation#ParameterDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.description
    import aws_sdk_cloudformation.types.no_echo
    import aws_sdk_cloudformation.types.parameter_constraints
    import aws_sdk_cloudformation.types.parameter_key
    import aws_sdk_cloudformation.types.parameter_type
    import aws_sdk_cloudformation.types.parameter_value


class ParameterDeclaration(TypedDict):
    parameter_key: NotRequired[
        "aws_sdk_cloudformation.types.parameter_key.ParameterKey"
    ]
    """<p>The name that's associated with the parameter.</p>"""
    default_value: NotRequired[
        "aws_sdk_cloudformation.types.parameter_value.ParameterValue"
    ]
    """<p>The default value of the parameter.</p>"""
    parameter_type: NotRequired[
        "aws_sdk_cloudformation.types.parameter_type.ParameterType"
    ]
    """<p>The type of parameter.</p>"""
    no_echo: NotRequired["aws_sdk_cloudformation.types.no_echo.NoEcho"]
    """<p>Flag that indicates whether the parameter value is shown as plain text in logs and in the Amazon Web Services Management Console.</p>"""
    description: NotRequired["aws_sdk_cloudformation.types.description.Description"]
    """<p>The description that's associate with the parameter.</p>"""
    parameter_constraints: NotRequired[
        "aws_sdk_cloudformation.types.parameter_constraints.ParameterConstraints"
    ]
    """<p>The criteria that CloudFormation uses to validate parameter values.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterDeclaration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_key" in value:
        pairs.append((f"{prefix}.ParameterKey", str(value["parameter_key"])))
    if "default_value" in value:
        pairs.append((f"{prefix}.DefaultValue", str(value["default_value"])))
    if "parameter_type" in value:
        pairs.append((f"{prefix}.ParameterType", str(value["parameter_type"])))
    if "no_echo" in value:
        pairs.append((f"{prefix}.NoEcho", "true" if value["no_echo"] else "false"))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "parameter_constraints" in value:
        import aws_sdk_cloudformation.types.parameter_constraints

        aws_sdk_cloudformation.types.parameter_constraints.serialize_query(
            value["parameter_constraints"], pairs, f"{prefix}.ParameterConstraints"
        )


def deserialize_query(el: Element) -> ParameterDeclaration:
    out: ParameterDeclaration = {}  # type: ignore[typeddict-item]
    child_parameter_key = el.find("ParameterKey")
    if child_parameter_key is not None:
        out["parameter_key"] = str(child_parameter_key.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_parameter_type = el.find("ParameterType")
    if child_parameter_type is not None:
        out["parameter_type"] = str(child_parameter_type.text or "")
    child_no_echo = el.find("NoEcho")
    if child_no_echo is not None:
        out["no_echo"] = (child_no_echo.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_parameter_constraints = el.find("ParameterConstraints")
    if child_parameter_constraints is not None:
        import aws_sdk_cloudformation.types.parameter_constraints

        out["parameter_constraints"] = (
            aws_sdk_cloudformation.types.parameter_constraints.deserialize_query(
                child_parameter_constraints
            )
        )
    return out
