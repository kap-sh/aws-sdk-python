"""Generated from Smithy shape ``com.amazonaws.opensearch#GetCompatibleVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.compatible_versions_list


class GetCompatibleVersionsResponse(TypedDict):
    compatible_versions: NotRequired[
        "aws_sdk_opensearch.types.compatible_versions_list.CompatibleVersionsList"
    ]
    """<p>A map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCompatibleVersionsResponse) -> dict:
    out: dict = {}
    if "compatible_versions" in value:
        import aws_sdk_opensearch.types.compatible_versions_list

        out["CompatibleVersions"] = (
            aws_sdk_opensearch.types.compatible_versions_list.serialize_json(
                value["compatible_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCompatibleVersionsResponse:
    out: GetCompatibleVersionsResponse = {}  # type: ignore[typeddict-item]
    if "CompatibleVersions" in data:
        import aws_sdk_opensearch.types.compatible_versions_list

        out["compatible_versions"] = (
            aws_sdk_opensearch.types.compatible_versions_list.deserialize_json(
                data["CompatibleVersions"]
            )
        )
    return out
