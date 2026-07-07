"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateThemeResponse(TypedDict, closed=True):
    theme_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the theme.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the theme.</p>"""
    version_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the new version of the theme.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The creation status of the theme.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemeResponse) -> dict:
    out: dict = {}
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_arn" in value:
        out["VersionArn"] = value["version_arn"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateThemeResponse:
    out: UpdateThemeResponse = {}  # type: ignore[typeddict-item]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VersionArn" in data:
        out["version_arn"] = data["VersionArn"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
