"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MultiLayerStorage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.customer_managed_s3_storage


class MultiLayerStorage(TypedDict):
    customer_managed_s3_storage: (
        "aws_sdk_iotsitewise.types.customer_managed_s3_storage.CustomerManagedS3Storage"
    )
    """<p>Contains information about a customer managed Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiLayerStorage) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.customer_managed_s3_storage

    out["customerManagedS3Storage"] = (
        aws_sdk_iotsitewise.types.customer_managed_s3_storage.serialize_json(
            value["customer_managed_s3_storage"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiLayerStorage:
    out: MultiLayerStorage = {}  # type: ignore[typeddict-item]
    if "customerManagedS3Storage" in data:
        import aws_sdk_iotsitewise.types.customer_managed_s3_storage

        out["customer_managed_s3_storage"] = (
            aws_sdk_iotsitewise.types.customer_managed_s3_storage.deserialize_json(
                data["customerManagedS3Storage"]
            )
        )
    else:
        raise DeserializationError(
            "MultiLayerStorage.customer_managed_s3_storage required"
        )
    return out
