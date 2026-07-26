"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.brand_definition
    import capo_quicksight.types.short_restrictive_resource_id


class UpdateBrandRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the Quick brand.</p>"""
    brand_definition: NotRequired[
        "capo_quicksight.types.brand_definition.BrandDefinition"
    ]
    """<p>The definition of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandRequest) -> dict:
    out: dict = {}
    if "brand_definition" in value:
        import capo_quicksight.types.brand_definition

        out["BrandDefinition"] = capo_quicksight.types.brand_definition.serialize_json(
            value["brand_definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBrandRequest:
    out: UpdateBrandRequest = {}  # type: ignore[typeddict-item]
    if "BrandDefinition" in data:
        import capo_quicksight.types.brand_definition

        out["brand_definition"] = (
            capo_quicksight.types.brand_definition.deserialize_json(
                data["BrandDefinition"]
            )
        )
    return out
