"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2PlatformVersionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.serverless_v2_features_support
    import aws_sdk_rds.types.string


class ServerlessV2PlatformVersionInfo(TypedDict, closed=True):
    serverless_v2_platform_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The version number of the serverless platform.</p>"""
    serverless_v2_platform_version_description: NotRequired[
        "aws_sdk_rds.types.string.String"
    ]
    """<p>The description of the serverless platform.</p>"""
    engine: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the database engine.</p>"""
    serverless_v2_features_support: NotRequired[
        "aws_sdk_rds.types.serverless_v2_features_support.ServerlessV2FeaturesSupport"
    ]
    """<p>Specifies any Aurora Serverless v2 properties or limits that differ between Aurora Serverless v2 platform versions. You can retrieve the platform version of an existing DB cluster and check whether that version supports certain Aurora Serverless v2 features before you attempt to use those features.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the serverless platform. Valid statuses are the following:</p> <ul> <li> <p> <code>enabled</code> - The platform version is in use.</p> </li> <li> <p> <code>disabled</code> - The platform version is not in use.</p> </li> </ul>"""
    is_default: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether this platform version is the default version for the engine. The default platform version is the version used for new DB clusters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2PlatformVersionInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_v2_platform_version" in value:
        pairs.append(
            (
                f"{prefix}.ServerlessV2PlatformVersion",
                str(value["serverless_v2_platform_version"]),
            )
        )
    if "serverless_v2_platform_version_description" in value:
        pairs.append(
            (
                f"{prefix}.ServerlessV2PlatformVersionDescription",
                str(value["serverless_v2_platform_version_description"]),
            )
        )
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "serverless_v2_features_support" in value:
        import aws_sdk_rds.types.serverless_v2_features_support

        aws_sdk_rds.types.serverless_v2_features_support.serialize_query(
            value["serverless_v2_features_support"],
            pairs,
            f"{prefix}.ServerlessV2FeaturesSupport",
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )


def deserialize_query(el: Element) -> ServerlessV2PlatformVersionInfo:
    out: ServerlessV2PlatformVersionInfo = {}  # type: ignore[typeddict-item]
    child_serverless_v2_platform_version = el.find("ServerlessV2PlatformVersion")
    if child_serverless_v2_platform_version is not None:
        out["serverless_v2_platform_version"] = str(
            child_serverless_v2_platform_version.text or ""
        )
    child_serverless_v2_platform_version_description = el.find(
        "ServerlessV2PlatformVersionDescription"
    )
    if child_serverless_v2_platform_version_description is not None:
        out["serverless_v2_platform_version_description"] = str(
            child_serverless_v2_platform_version_description.text or ""
        )
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_serverless_v2_features_support = el.find("ServerlessV2FeaturesSupport")
    if child_serverless_v2_features_support is not None:
        import aws_sdk_rds.types.serverless_v2_features_support

        out["serverless_v2_features_support"] = (
            aws_sdk_rds.types.serverless_v2_features_support.deserialize_query(
                child_serverless_v2_features_support
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    return out
