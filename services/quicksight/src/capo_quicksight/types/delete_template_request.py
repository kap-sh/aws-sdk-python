"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.version_number


class DeleteTemplateRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template that you're deleting.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the template you want to delete.</p>"""
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>Specifies the version of the template that you want to delete. If you don't provide a version number, <code>DeleteTemplate</code> deletes all versions of the template. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTemplateRequest:
    out: DeleteTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
