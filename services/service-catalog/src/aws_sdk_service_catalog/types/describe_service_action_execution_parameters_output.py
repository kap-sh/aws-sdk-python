"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionExecutionParametersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.execution_parameters


class DescribeServiceActionExecutionParametersOutput(TypedDict):
    service_action_parameters: NotRequired[
        "aws_sdk_service_catalog.types.execution_parameters.ExecutionParameters"
    ]
    """<p>The parameters of the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeServiceActionExecutionParametersOutput,
) -> dict:
    out: dict = {}
    if "service_action_parameters" in value:
        import aws_sdk_service_catalog.types.execution_parameters

        out["ServiceActionParameters"] = (
            aws_sdk_service_catalog.types.execution_parameters.serialize_aws_json_1_1(
                value["service_action_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeServiceActionExecutionParametersOutput:
    out: DescribeServiceActionExecutionParametersOutput = {}  # type: ignore[typeddict-item]
    if "ServiceActionParameters" in data:
        import aws_sdk_service_catalog.types.execution_parameters

        out["service_action_parameters"] = (
            aws_sdk_service_catalog.types.execution_parameters.deserialize_aws_json_1_1(
                data["ServiceActionParameters"]
            )
        )
    return out
