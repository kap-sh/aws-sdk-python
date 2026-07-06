"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateBrandRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.brand_definition
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.tag_list


class CreateBrandRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the Quick brand.</p>"""
    brand_definition: NotRequired[
        "aws_sdk_quicksight.types.brand_definition.BrandDefinition"
    ]
    """<p>The definition of the brand.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>A map of the key-value pairs that are assigned to the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrandRequest) -> dict:
    out: dict = {}
    if "brand_definition" in value:
        import aws_sdk_quicksight.types.brand_definition

        out["BrandDefinition"] = (
            aws_sdk_quicksight.types.brand_definition.serialize_json(
                value["brand_definition"]
            )
        )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBrandRequest:
    out: CreateBrandRequest = {}  # type: ignore[typeddict-item]
    if "BrandDefinition" in data:
        import aws_sdk_quicksight.types.brand_definition

        out["brand_definition"] = (
            aws_sdk_quicksight.types.brand_definition.deserialize_json(
                data["BrandDefinition"]
            )
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
