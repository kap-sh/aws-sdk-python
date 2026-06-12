"""Generated from Smithy shape ``com.amazonaws.opensearch#CompatibleVersionsMap``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.version_list
    import aws_sdk_opensearch.types.version_string


class CompatibleVersionsMap(TypedDict):
    source_version: NotRequired["aws_sdk_opensearch.types.version_string.VersionString"]
    """<p>The current version that the OpenSearch Service domain is running.</p>"""
    target_versions: NotRequired["aws_sdk_opensearch.types.version_list.VersionList"]
    """<p>The possible versions that you can upgrade the domain to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleVersionsMap) -> dict:
    out: dict = {}
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    if "target_versions" in value:
        import aws_sdk_opensearch.types.version_list

        out["TargetVersions"] = aws_sdk_opensearch.types.version_list.serialize_json(
            value["target_versions"]
        )
    return out


def deserialize_json(data: dict) -> CompatibleVersionsMap:
    out: CompatibleVersionsMap = {}  # type: ignore[typeddict-item]
    if "SourceVersion" in data:
        out["source_version"] = data["SourceVersion"]
    if "TargetVersions" in data:
        import aws_sdk_opensearch.types.version_list

        out["target_versions"] = aws_sdk_opensearch.types.version_list.deserialize_json(
            data["TargetVersions"]
        )
    return out
