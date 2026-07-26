"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftStorage``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.redshift_cluster_storage
    import capo_datazone.types.redshift_serverless_storage


class _RedshiftStorage_redshiftClusterSource(TypedDict, closed=True):
    redshiftClusterSource: (
        "capo_datazone.types.redshift_cluster_storage.RedshiftClusterStorage"
    )


class _RedshiftStorage_redshiftServerlessSource(TypedDict, closed=True):
    redshiftServerlessSource: (
        "capo_datazone.types.redshift_serverless_storage.RedshiftServerlessStorage"
    )


RedshiftStorage: TypeAlias = (
    _RedshiftStorage_redshiftClusterSource | _RedshiftStorage_redshiftServerlessSource
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftStorage) -> dict:
    if "redshiftClusterSource" in value:
        import capo_datazone.types.redshift_cluster_storage

        return {
            "redshiftClusterSource": capo_datazone.types.redshift_cluster_storage.serialize_json(
                value["redshiftClusterSource"]
            )
        }
    elif "redshiftServerlessSource" in value:
        import capo_datazone.types.redshift_serverless_storage

        return {
            "redshiftServerlessSource": capo_datazone.types.redshift_serverless_storage.serialize_json(
                value["redshiftServerlessSource"]
            )
        }
    else:
        raise SerializationError("RedshiftStorage: no variant present")


def deserialize_json(data: dict) -> RedshiftStorage:
    if "redshiftClusterSource" in data:
        import capo_datazone.types.redshift_cluster_storage

        return {
            "redshiftClusterSource": capo_datazone.types.redshift_cluster_storage.deserialize_json(
                data["redshiftClusterSource"]
            )
        }
    elif "redshiftServerlessSource" in data:
        import capo_datazone.types.redshift_serverless_storage

        return {
            "redshiftServerlessSource": capo_datazone.types.redshift_serverless_storage.deserialize_json(
                data["redshiftServerlessSource"]
            )
        }
    else:
        raise DeserializationError("RedshiftStorage: no recognized variant key")
