"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteServerlessCacheSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class DeleteServerlessCacheSnapshotRequest(TypedDict):
    serverless_cache_snapshot_name: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>Idenfitier of the snapshot to be deleted. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServerlessCacheSnapshotRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{prefix}.ServerlessCacheSnapshotName",
                str(value["serverless_cache_snapshot_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteServerlessCacheSnapshotRequest:
    out: DeleteServerlessCacheSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    return out
