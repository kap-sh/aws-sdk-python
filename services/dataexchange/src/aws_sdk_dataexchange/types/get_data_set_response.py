"""Generated from Smithy shape ``com.amazonaws.dataexchange#GetDataSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.asset_type
    import aws_sdk_dataexchange.types.description
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.map_of__string
    import aws_sdk_dataexchange.types.name
    import aws_sdk_dataexchange.types.origin
    import aws_sdk_dataexchange.types.origin_details
    import aws_sdk_dataexchange.types.timestamp


class GetDataSetResponse(TypedDict):
    arn: NotRequired["aws_sdk_dataexchange.types.arn.Arn"]
    """<p>The ARN for the data set.</p>"""
    asset_type: NotRequired["aws_sdk_dataexchange.types.asset_type.AssetType"]
    """<p>The type of asset that is added to a data set.</p>"""
    created_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the data set was created, in ISO 8601 format.</p>"""
    description: NotRequired["aws_sdk_dataexchange.types.description.Description"]
    """<p>The description for the data set.</p>"""
    id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The unique identifier for the data set.</p>"""
    name: NotRequired["aws_sdk_dataexchange.types.name.Name"]
    """<p>The name of the data set.</p>"""
    origin: NotRequired["aws_sdk_dataexchange.types.origin.Origin"]
    """<p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>"""
    origin_details: NotRequired[
        "aws_sdk_dataexchange.types.origin_details.OriginDetails"
    ]
    """<p>If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.</p>"""
    source_id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.</p>"""
    tags: NotRequired["aws_sdk_dataexchange.types.map_of__string.MapOf__string"]
    """<p>The tags for the data set.</p>"""
    updated_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the data set was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "asset_type" in value:
        out["AssetType"] = value["asset_type"]
    if "created_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "origin" in value:
        out["Origin"] = value["origin"]
    if "origin_details" in value:
        import aws_sdk_dataexchange.types.origin_details

        out["OriginDetails"] = aws_sdk_dataexchange.types.origin_details.serialize_json(
            value["origin_details"]
        )
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "tags" in value:
        import aws_sdk_dataexchange.types.map_of__string

        out["Tags"] = aws_sdk_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    if "updated_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetDataSetResponse:
    out: GetDataSetResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AssetType" in data:
        out["asset_type"] = data["AssetType"]
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Origin" in data:
        out["origin"] = data["Origin"]
    if "OriginDetails" in data:
        import aws_sdk_dataexchange.types.origin_details

        out["origin_details"] = (
            aws_sdk_dataexchange.types.origin_details.deserialize_json(
                data["OriginDetails"]
            )
        )
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    if "Tags" in data:
        import aws_sdk_dataexchange.types.map_of__string

        out["tags"] = aws_sdk_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
