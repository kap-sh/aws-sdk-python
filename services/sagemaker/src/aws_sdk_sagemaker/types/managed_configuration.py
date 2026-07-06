"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.managed_storage_type


class ManagedConfiguration(TypedDict, closed=True):
    managed_storage_type: NotRequired[
        "aws_sdk_sagemaker.types.managed_storage_type.ManagedStorageType"
    ]
    """<p>The storage type of the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedConfiguration) -> dict:
    out: dict = {}
    if "managed_storage_type" in value:
        import aws_sdk_sagemaker.types.managed_storage_type

        out["ManagedStorageType"] = (
            aws_sdk_sagemaker.types.managed_storage_type.serialize_aws_json_1_1(
                value["managed_storage_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedConfiguration:
    out: ManagedConfiguration = {}  # type: ignore[typeddict-item]
    if "ManagedStorageType" in data:
        import aws_sdk_sagemaker.types.managed_storage_type

        out["managed_storage_type"] = (
            aws_sdk_sagemaker.types.managed_storage_type.deserialize_aws_json_1_1(
                data["ManagedStorageType"]
            )
        )
    return out
