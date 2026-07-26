"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeScalingParametersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.scaling_parameters_status


class DescribeScalingParametersResponse(TypedDict, closed=True):
    scaling_parameters: (
        "capo_cloudsearch.types.scaling_parameters_status.ScalingParametersStatus"
    )


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScalingParametersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.scaling_parameters_status

    capo_cloudsearch.types.scaling_parameters_status.serialize_query(
        value["scaling_parameters"], pairs, f"{prefix}.ScalingParameters"
    )


def deserialize_query(el: Element) -> DescribeScalingParametersResponse:
    out: DescribeScalingParametersResponse = {}  # type: ignore[typeddict-item]
    child_scaling_parameters = el.find("ScalingParameters")
    if child_scaling_parameters is not None:
        import capo_cloudsearch.types.scaling_parameters_status

        out["scaling_parameters"] = (
            capo_cloudsearch.types.scaling_parameters_status.deserialize_query(
                child_scaling_parameters
            )
        )
    else:
        raise DeserializationError(
            "DescribeScalingParametersResponse.scaling_parameters required"
        )
    return out
