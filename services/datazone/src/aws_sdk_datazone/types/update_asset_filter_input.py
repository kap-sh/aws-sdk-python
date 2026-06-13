"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateAssetFilterInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_filter_configuration
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_id


class UpdateAssetFilterInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to update an asset filter.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    identifier: "aws_sdk_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""
    name: NotRequired["str"]
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    configuration: NotRequired[
        "aws_sdk_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    ]
    """<p>The configuration of the asset filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetFilterInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "configuration" in value:
        import aws_sdk_datazone.types.asset_filter_configuration

        out["configuration"] = (
            aws_sdk_datazone.types.asset_filter_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssetFilterInput:
    out: UpdateAssetFilterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "configuration" in data:
        import aws_sdk_datazone.types.asset_filter_configuration

        out["configuration"] = (
            aws_sdk_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
