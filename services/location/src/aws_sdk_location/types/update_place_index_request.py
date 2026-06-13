"""Generated from Smithy shape ``com.amazonaws.location#UpdatePlaceIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.data_source_configuration
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name


class UpdatePlaceIndexRequest(TypedDict):
    index_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource to update.</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    description: NotRequired[
        "aws_sdk_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the place index resource.</p>"""
    data_source_configuration: NotRequired[
        "aws_sdk_location.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>Updates the data storage option for the place index resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePlaceIndexRequest) -> dict:
    out: dict = {}
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_source_configuration" in value:
        import aws_sdk_location.types.data_source_configuration

        out["DataSourceConfiguration"] = (
            aws_sdk_location.types.data_source_configuration.serialize_json(
                value["data_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePlaceIndexRequest:
    out: UpdatePlaceIndexRequest = {}  # type: ignore[typeddict-item]
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DataSourceConfiguration" in data:
        import aws_sdk_location.types.data_source_configuration

        out["data_source_configuration"] = (
            aws_sdk_location.types.data_source_configuration.deserialize_json(
                data["DataSourceConfiguration"]
            )
        )
    return out
