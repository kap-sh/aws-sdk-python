"""Generated from Smithy shape ``com.amazonaws.rds#ServerlessV2PlatformVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.serverless_v2_platform_version_info

ServerlessV2PlatformVersionList: TypeAlias = list[
    "aws_sdk_rds.types.serverless_v2_platform_version_info.ServerlessV2PlatformVersionInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessV2PlatformVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.serverless_v2_platform_version_info

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.serverless_v2_platform_version_info.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServerlessV2PlatformVersionList:
    import aws_sdk_rds.types.serverless_v2_platform_version_info

    out: ServerlessV2PlatformVersionList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_rds.types.serverless_v2_platform_version_info.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ServerlessV2PlatformVersionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.serverless_v2_platform_version_info

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.serverless_v2_platform_version_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ServerlessV2PlatformVersionList:
    import aws_sdk_rds.types.serverless_v2_platform_version_info

    out: ServerlessV2PlatformVersionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.serverless_v2_platform_version_info.deserialize_query(
                child
            )
        )
    return out
