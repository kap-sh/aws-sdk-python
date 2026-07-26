"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SyntheticDataParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.ml_synthetic_data_parameters


class _SyntheticDataParameters_mlSyntheticDataParameters(TypedDict, closed=True):
    mlSyntheticDataParameters: (
        "capo_cleanrooms.types.ml_synthetic_data_parameters.MLSyntheticDataParameters"
    )


SyntheticDataParameters: TypeAlias = _SyntheticDataParameters_mlSyntheticDataParameters


# --- restJson1 ser/de ---
def serialize_json(value: SyntheticDataParameters) -> dict:
    if "mlSyntheticDataParameters" in value:
        import capo_cleanrooms.types.ml_synthetic_data_parameters

        return {
            "mlSyntheticDataParameters": capo_cleanrooms.types.ml_synthetic_data_parameters.serialize_json(
                value["mlSyntheticDataParameters"]
            )
        }
    else:
        raise SerializationError("SyntheticDataParameters: no variant present")


def deserialize_json(data: dict) -> SyntheticDataParameters:
    if "mlSyntheticDataParameters" in data:
        import capo_cleanrooms.types.ml_synthetic_data_parameters

        return {
            "mlSyntheticDataParameters": capo_cleanrooms.types.ml_synthetic_data_parameters.deserialize_json(
                data["mlSyntheticDataParameters"]
            )
        }
    else:
        raise DeserializationError("SyntheticDataParameters: no recognized variant key")
