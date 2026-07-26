"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.arn
    import capo_quicksight.types.brand_status
    import capo_quicksight.types.description
    import capo_quicksight.types.name
    import capo_quicksight.types.short_restrictive_resource_id


class BrandSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""
    brand_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the Quick brand.</p>"""
    brand_name: NotRequired["capo_quicksight.types.name.Name"]
    """<p>The name of the brand.</p>"""
    description: NotRequired["capo_quicksight.types.description.Description"]
    """<p>The description of the brand.</p>"""
    brand_status: NotRequired["capo_quicksight.types.brand_status.BrandStatus"]
    """<p>The status of the brand.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The time that the brand was created.</p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p>The time when the brand was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "brand_id" in value:
        out["BrandId"] = value["brand_id"]
    if "brand_name" in value:
        out["BrandName"] = value["brand_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "brand_status" in value:
        import capo_quicksight.types.brand_status

        out["BrandStatus"] = capo_quicksight.types.brand_status.serialize_json(
            value["brand_status"]
        )
    if "created_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["CreatedTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["LastUpdatedTime"] = (
            capo_quicksight.types._prelude.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrandSummary:
    out: BrandSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "BrandId" in data:
        out["brand_id"] = data["BrandId"]
    if "BrandName" in data:
        out["brand_name"] = data["BrandName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "BrandStatus" in data:
        import capo_quicksight.types.brand_status

        out["brand_status"] = capo_quicksight.types.brand_status.deserialize_json(
            data["BrandStatus"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types._prelude.timestamp

        out["created_time"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_quicksight.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
