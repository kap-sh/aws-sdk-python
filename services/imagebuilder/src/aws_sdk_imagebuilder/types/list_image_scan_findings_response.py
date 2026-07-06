"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageScanFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_scan_findings_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListImageScanFindingsResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    findings: NotRequired[
        "aws_sdk_imagebuilder.types.image_scan_findings_list.ImageScanFindingsList"
    ]
    """<p>The image scan findings for your account that meet your request filter criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageScanFindingsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "findings" in value:
        import aws_sdk_imagebuilder.types.image_scan_findings_list

        out["findings"] = (
            aws_sdk_imagebuilder.types.image_scan_findings_list.serialize_json(
                value["findings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageScanFindingsResponse:
    out: ListImageScanFindingsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "findings" in data:
        import aws_sdk_imagebuilder.types.image_scan_findings_list

        out["findings"] = (
            aws_sdk_imagebuilder.types.image_scan_findings_list.deserialize_json(
                data["findings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
