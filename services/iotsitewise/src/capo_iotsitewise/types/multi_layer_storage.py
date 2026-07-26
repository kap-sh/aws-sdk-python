"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MultiLayerStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.customer_managed_s3_storage


class MultiLayerStorage(TypedDict, closed=True):
    customer_managed_s3_storage: (
        "capo_iotsitewise.types.customer_managed_s3_storage.CustomerManagedS3Storage"
    )
    """<p>Contains information about a customer managed Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiLayerStorage) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.customer_managed_s3_storage

    out["customerManagedS3Storage"] = (
        capo_iotsitewise.types.customer_managed_s3_storage.serialize_json(
            value["customer_managed_s3_storage"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiLayerStorage:
    out: MultiLayerStorage = {}  # type: ignore[typeddict-item]
    if "customerManagedS3Storage" in data:
        import capo_iotsitewise.types.customer_managed_s3_storage

        out["customer_managed_s3_storage"] = (
            capo_iotsitewise.types.customer_managed_s3_storage.deserialize_json(
                data["customerManagedS3Storage"]
            )
        )
    else:
        raise DeserializationError(
            "MultiLayerStorage.customer_managed_s3_storage required"
        )
    return out
