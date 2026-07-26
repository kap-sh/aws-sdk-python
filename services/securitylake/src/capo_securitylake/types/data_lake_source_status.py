"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.source_collection_status


class DataLakeSourceStatus(TypedDict, closed=True):
    resource: NotRequired["str"]
    """<p>Defines path the stored logs are available which has information on your systems, applications, and services.</p>"""
    status: NotRequired[
        "capo_securitylake.types.source_collection_status.SourceCollectionStatus"
    ]
    """<p>The health status of services, including error codes and patterns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSourceStatus) -> dict:
    out: dict = {}
    if "resource" in value:
        out["resource"] = value["resource"]
    if "status" in value:
        import capo_securitylake.types.source_collection_status

        out["status"] = capo_securitylake.types.source_collection_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DataLakeSourceStatus:
    out: DataLakeSourceStatus = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "status" in data:
        import capo_securitylake.types.source_collection_status

        out["status"] = (
            capo_securitylake.types.source_collection_status.deserialize_json(
                data["status"]
            )
        )
    return out
