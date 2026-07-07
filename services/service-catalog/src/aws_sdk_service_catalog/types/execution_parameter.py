"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecutionParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.execution_parameter_key
    import aws_sdk_service_catalog.types.execution_parameter_type
    import aws_sdk_service_catalog.types.execution_parameter_value_list


class ExecutionParameter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_service_catalog.types.execution_parameter_key.ExecutionParameterKey"
    ]
    """<p>The name of the execution parameter.</p>"""
    type: NotRequired[
        "aws_sdk_service_catalog.types.execution_parameter_type.ExecutionParameterType"
    ]
    """<p>The execution parameter type.</p>"""
    default_values: NotRequired[
        "aws_sdk_service_catalog.types.execution_parameter_value_list.ExecutionParameterValueList"
    ]
    """<p>The default values for the execution parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "default_values" in value:
        import aws_sdk_service_catalog.types.execution_parameter_value_list

        out["DefaultValues"] = (
            aws_sdk_service_catalog.types.execution_parameter_value_list.serialize_aws_json_1_1(
                value["default_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionParameter:
    out: ExecutionParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "DefaultValues" in data:
        import aws_sdk_service_catalog.types.execution_parameter_value_list

        out["default_values"] = (
            aws_sdk_service_catalog.types.execution_parameter_value_list.deserialize_aws_json_1_1(
                data["DefaultValues"]
            )
        )
    return out
