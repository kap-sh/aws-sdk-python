"""Generated from Smithy shape ``com.amazonaws.omics#DeleteAnnotationStoreVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.version_list


class DeleteAnnotationStoreVersionsRequest(TypedDict):
    name: "str"
    """<p> The name of the annotation store from which versions are being deleted. </p>"""
    versions: "aws_sdk_omics.types.version_list.VersionList"
    """<p> The versions of an annotation store to be deleted. </p>"""
    force: "bool"
    """<p> Forces the deletion of an annotation store version when imports are in-progress.. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnnotationStoreVersionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_omics.types.version_list

    out["versions"] = aws_sdk_omics.types.version_list.serialize_json(value["versions"])
    return out


def deserialize_json(data: dict) -> DeleteAnnotationStoreVersionsRequest:
    out: DeleteAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
    if "versions" in data:
        import aws_sdk_omics.types.version_list

        out["versions"] = aws_sdk_omics.types.version_list.deserialize_json(
            data["versions"]
        )
    else:
        raise DeserializationError(
            "DeleteAnnotationStoreVersionsRequest.versions required"
        )
    return out
