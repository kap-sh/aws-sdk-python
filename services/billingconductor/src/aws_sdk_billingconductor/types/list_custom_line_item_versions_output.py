"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_version_list
    import aws_sdk_billingconductor.types.token


class ListCustomLineItemVersionsOutput(TypedDict):
    custom_line_item_versions: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_version_list.CustomLineItemVersionList"
    ]
    """<p>A list of <code>CustomLineItemVersionListElements</code> that are received.</p>"""
    next_token: NotRequired["aws_sdk_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsOutput) -> dict:
    out: dict = {}
    if "custom_line_item_versions" in value:
        import aws_sdk_billingconductor.types.custom_line_item_version_list

        out["CustomLineItemVersions"] = (
            aws_sdk_billingconductor.types.custom_line_item_version_list.serialize_json(
                value["custom_line_item_versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsOutput:
    out: ListCustomLineItemVersionsOutput = {}  # type: ignore[typeddict-item]
    if "CustomLineItemVersions" in data:
        import aws_sdk_billingconductor.types.custom_line_item_version_list

        out["custom_line_item_versions"] = (
            aws_sdk_billingconductor.types.custom_line_item_version_list.deserialize_json(
                data["CustomLineItemVersions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
