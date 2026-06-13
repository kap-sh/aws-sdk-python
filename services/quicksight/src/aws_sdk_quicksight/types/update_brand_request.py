"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.brand_definition
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class UpdateBrandRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the Quick brand.</p>"""
    brand_definition: NotRequired[
        "aws_sdk_quicksight.types.brand_definition.BrandDefinition"
    ]
    """<p>The definition of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandRequest) -> dict:
    out: dict = {}
    if "brand_definition" in value:
        import aws_sdk_quicksight.types.brand_definition

        out["BrandDefinition"] = (
            aws_sdk_quicksight.types.brand_definition.serialize_json(
                value["brand_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBrandRequest:
    out: UpdateBrandRequest = {}  # type: ignore[typeddict-item]
    if "BrandDefinition" in data:
        import aws_sdk_quicksight.types.brand_definition

        out["brand_definition"] = (
            aws_sdk_quicksight.types.brand_definition.deserialize_json(
                data["BrandDefinition"]
            )
        )
    return out
