"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeScalingParametersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.scaling_parameters_status


class DescribeScalingParametersResponse(TypedDict):
    scaling_parameters: (
        "aws_sdk_cloudsearch.types.scaling_parameters_status.ScalingParametersStatus"
    )


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScalingParametersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.scaling_parameters_status

    aws_sdk_cloudsearch.types.scaling_parameters_status.serialize_query(
        value["scaling_parameters"], pairs, f"{prefix}.ScalingParameters"
    )


def deserialize_query(el: Element) -> DescribeScalingParametersResponse:
    out: DescribeScalingParametersResponse = {}  # type: ignore[typeddict-item]
    child_scaling_parameters = el.find("ScalingParameters")
    if child_scaling_parameters is not None:
        import aws_sdk_cloudsearch.types.scaling_parameters_status

        out["scaling_parameters"] = (
            aws_sdk_cloudsearch.types.scaling_parameters_status.deserialize_query(
                child_scaling_parameters
            )
        )
    else:
        raise DeserializationError(
            "DescribeScalingParametersResponse.scaling_parameters required"
        )
    return out
