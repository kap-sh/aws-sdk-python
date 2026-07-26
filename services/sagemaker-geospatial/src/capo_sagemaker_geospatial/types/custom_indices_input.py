"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#CustomIndicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.operations_list_input


class CustomIndicesInput(TypedDict, closed=True):
    operations: NotRequired[
        "capo_sagemaker_geospatial.types.operations_list_input.OperationsListInput"
    ]
    """<p>A list of BandMath indices to compute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomIndicesInput) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_sagemaker_geospatial.types.operations_list_input

        out["Operations"] = (
            capo_sagemaker_geospatial.types.operations_list_input.serialize_json(
                value["operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomIndicesInput:
    out: CustomIndicesInput = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import capo_sagemaker_geospatial.types.operations_list_input

        out["operations"] = (
            capo_sagemaker_geospatial.types.operations_list_input.deserialize_json(
                data["Operations"]
            )
        )
    return out
