"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateScalingParametersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.scaling_parameters_status


class UpdateScalingParametersResponse(TypedDict, closed=True):
    scaling_parameters: (
        "aws_sdk_cloudsearch.types.scaling_parameters_status.ScalingParametersStatus"
    )


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateScalingParametersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.scaling_parameters_status

    aws_sdk_cloudsearch.types.scaling_parameters_status.serialize_query(
        value["scaling_parameters"], pairs, f"{prefix}.ScalingParameters"
    )


def deserialize_query(el: Element) -> UpdateScalingParametersResponse:
    out: UpdateScalingParametersResponse = {}  # type: ignore[typeddict-item]
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
            "UpdateScalingParametersResponse.scaling_parameters required"
        )
    return out
