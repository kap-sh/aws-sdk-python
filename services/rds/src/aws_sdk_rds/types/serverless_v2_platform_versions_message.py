"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2PlatformVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.serverless_v2_platform_version_list
    import aws_sdk_rds.types.string


class ServerlessV2PlatformVersionsMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    serverless_v2_platform_versions: NotRequired[
        "aws_sdk_rds.types.serverless_v2_platform_version_list.ServerlessV2PlatformVersionList"
    ]
    """<p>A list of <code>ServerlessV2PlatformVersionInfo</code> elements.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2PlatformVersionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "serverless_v2_platform_versions" in value:
        import aws_sdk_rds.types.serverless_v2_platform_version_list

        aws_sdk_rds.types.serverless_v2_platform_version_list.serialize_query(
            value["serverless_v2_platform_versions"],
            pairs,
            f"{prefix}.ServerlessV2PlatformVersions",
        )


def deserialize_query(el: Element) -> ServerlessV2PlatformVersionsMessage:
    out: ServerlessV2PlatformVersionsMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_serverless_v2_platform_versions = el.find("ServerlessV2PlatformVersions")
    if child_serverless_v2_platform_versions is not None:
        import aws_sdk_rds.types.serverless_v2_platform_version_list

        out["serverless_v2_platform_versions"] = (
            aws_sdk_rds.types.serverless_v2_platform_version_list.deserialize_query(
                child_serverless_v2_platform_versions
            )
        )
    return out
