"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketStorageClassResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.storage_class_configuration


class GetTableBucketStorageClassResponse(TypedDict, closed=True):
    storage_class_configuration: (
        "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
    )
    """<p>The storage class configuration for the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketStorageClassResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.storage_class_configuration

    out["storageClassConfiguration"] = (
        capo_s3tables.types.storage_class_configuration.serialize_json(
            value["storage_class_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableBucketStorageClassResponse:
    out: GetTableBucketStorageClassResponse = {}  # type: ignore[typeddict-item]
    if "storageClassConfiguration" in data:
        import capo_s3tables.types.storage_class_configuration

        out["storage_class_configuration"] = (
            capo_s3tables.types.storage_class_configuration.deserialize_json(
                data["storageClassConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableBucketStorageClassResponse.storage_class_configuration required"
        )
    return out
