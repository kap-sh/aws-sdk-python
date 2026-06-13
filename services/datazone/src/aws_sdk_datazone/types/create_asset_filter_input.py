"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAssetFilterInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_filter_configuration
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_name


class CreateAssetFilterInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which you want to create an asset filter.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    name: "aws_sdk_datazone.types.filter_name.FilterName"
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    configuration: (
        "aws_sdk_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    )
    """<p>The configuration of the asset filter.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssetFilterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_datazone.types.asset_filter_configuration

    out["configuration"] = (
        aws_sdk_datazone.types.asset_filter_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAssetFilterInput:
    out: CreateAssetFilterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssetFilterInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "configuration" in data:
        import aws_sdk_datazone.types.asset_filter_configuration

        out["configuration"] = (
            aws_sdk_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("CreateAssetFilterInput.configuration required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
