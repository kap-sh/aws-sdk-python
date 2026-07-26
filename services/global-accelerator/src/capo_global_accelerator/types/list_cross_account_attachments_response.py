"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCrossAccountAttachmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.attachments
    import capo_global_accelerator.types.generic_string


class ListCrossAccountAttachmentsResponse(TypedDict, closed=True):
    cross_account_attachments: NotRequired[
        "capo_global_accelerator.types.attachments.Attachments"
    ]
    """<p>Information about the cross-account attachments.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrossAccountAttachmentsResponse) -> dict:
    out: dict = {}
    if "cross_account_attachments" in value:
        import capo_global_accelerator.types.attachments

        out["CrossAccountAttachments"] = (
            capo_global_accelerator.types.attachments.serialize_aws_json_1_1(
                value["cross_account_attachments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrossAccountAttachmentsResponse:
    out: ListCrossAccountAttachmentsResponse = {}  # type: ignore[typeddict-item]
    if "CrossAccountAttachments" in data:
        import capo_global_accelerator.types.attachments

        out["cross_account_attachments"] = (
            capo_global_accelerator.types.attachments.deserialize_aws_json_1_1(
                data["CrossAccountAttachments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
