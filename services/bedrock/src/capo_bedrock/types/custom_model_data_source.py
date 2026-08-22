"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDataSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.model_package_arn_data_source


class _CustomModelDataSource_modelPackageArnDataSource(TypedDict, closed=True):
    modelPackageArnDataSource: (
        "capo_bedrock.types.model_package_arn_data_source.ModelPackageArnDataSource"
    )


CustomModelDataSource: TypeAlias = _CustomModelDataSource_modelPackageArnDataSource


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDataSource) -> dict:
    if "modelPackageArnDataSource" in value:
        import capo_bedrock.types.model_package_arn_data_source

        return {
            "modelPackageArnDataSource": capo_bedrock.types.model_package_arn_data_source.serialize_json(
                value["modelPackageArnDataSource"]
            )
        }
    else:
        raise SerializationError("CustomModelDataSource: no variant present")


def deserialize_json(data: dict) -> CustomModelDataSource:
    if data.get("modelPackageArnDataSource") is not None:
        import capo_bedrock.types.model_package_arn_data_source

        return {
            "modelPackageArnDataSource": capo_bedrock.types.model_package_arn_data_source.deserialize_json(
                data["modelPackageArnDataSource"]
            )
        }
    else:
        raise DeserializationError("CustomModelDataSource: no recognized variant key")
