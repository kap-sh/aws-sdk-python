"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteThemeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.version_number


class DeleteThemeRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the theme that you're deleting.</p>"""
    theme_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An ID for the theme that you want to delete.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version of the theme that you want to delete. </p> <p> <b>Note:</b> If you don't provide a version number, you're using this call to <code>DeleteTheme</code> to delete all versions of the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThemeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteThemeRequest:
    out: DeleteThemeRequest = {}  # type: ignore[typeddict-item]
    return out
