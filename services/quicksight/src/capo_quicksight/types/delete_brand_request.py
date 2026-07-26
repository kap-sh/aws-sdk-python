"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteBrandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DeleteBrandRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the Quick brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrandRequest:
    out: DeleteBrandRequest = {}  # type: ignore[typeddict-item]
    return out
