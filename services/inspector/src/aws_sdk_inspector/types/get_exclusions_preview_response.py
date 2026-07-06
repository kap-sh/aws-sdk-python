"""Generated from Smithy shape ``com.amazonaws.inspector#GetExclusionsPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.exclusion_preview_list
    import aws_sdk_inspector.types.pagination_token
    import aws_sdk_inspector.types.preview_status


class GetExclusionsPreviewResponse(TypedDict, closed=True):
    preview_status: "aws_sdk_inspector.types.preview_status.PreviewStatus"
    """<p>Specifies the status of the request to generate an exclusions preview.</p>"""
    exclusion_previews: NotRequired[
        "aws_sdk_inspector.types.exclusion_preview_list.ExclusionPreviewList"
    ]
    """<p>Information about the exclusions included in the preview.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExclusionsPreviewResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.preview_status

    out["previewStatus"] = (
        aws_sdk_inspector.types.preview_status.serialize_aws_json_1_1(
            value["preview_status"]
        )
    )
    if "exclusion_previews" in value:
        import aws_sdk_inspector.types.exclusion_preview_list

        out["exclusionPreviews"] = (
            aws_sdk_inspector.types.exclusion_preview_list.serialize_aws_json_1_1(
                value["exclusion_previews"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExclusionsPreviewResponse:
    out: GetExclusionsPreviewResponse = {}  # type: ignore[typeddict-item]
    if "previewStatus" in data:
        import aws_sdk_inspector.types.preview_status

        out["preview_status"] = (
            aws_sdk_inspector.types.preview_status.deserialize_aws_json_1_1(
                data["previewStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetExclusionsPreviewResponse.preview_status required"
        )
    if "exclusionPreviews" in data:
        import aws_sdk_inspector.types.exclusion_preview_list

        out["exclusion_previews"] = (
            aws_sdk_inspector.types.exclusion_preview_list.deserialize_aws_json_1_1(
                data["exclusionPreviews"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
