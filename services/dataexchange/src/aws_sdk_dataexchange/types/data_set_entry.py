"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataSetEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.asset_type
    import aws_sdk_dataexchange.types.description
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.name
    import aws_sdk_dataexchange.types.origin
    import aws_sdk_dataexchange.types.origin_details
    import aws_sdk_dataexchange.types.timestamp


class DataSetEntry(TypedDict):
    arn: "aws_sdk_dataexchange.types.arn.Arn"
    """<p>The ARN for the data set.</p>"""
    asset_type: "aws_sdk_dataexchange.types.asset_type.AssetType"
    """<p>The type of asset that is added to a data set.</p>"""
    created_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the data set was created, in ISO 8601 format.</p>"""
    description: "aws_sdk_dataexchange.types.description.Description"
    """<p>The description for the data set.</p>"""
    id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set.</p>"""
    name: "aws_sdk_dataexchange.types.name.Name"
    """<p>The name of the data set.</p>"""
    origin: "aws_sdk_dataexchange.types.origin.Origin"
    """<p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>"""
    origin_details: NotRequired[
        "aws_sdk_dataexchange.types.origin_details.OriginDetails"
    ]
    """<p>If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.</p>"""
    source_id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.</p>"""
    updated_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the data set was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetEntry) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AssetType"] = value["asset_type"]
    import aws_sdk_dataexchange.types.timestamp

    out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    out["Description"] = value["description"]
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    out["Origin"] = value["origin"]
    if "origin_details" in value:
        import aws_sdk_dataexchange.types.origin_details

        out["OriginDetails"] = aws_sdk_dataexchange.types.origin_details.serialize_json(
            value["origin_details"]
        )
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    import aws_sdk_dataexchange.types.timestamp

    out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DataSetEntry:
    out: DataSetEntry = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DataSetEntry.arn required")
    if "AssetType" in data:
        out["asset_type"] = data["AssetType"]
    else:
        raise DeserializationError("DataSetEntry.asset_type required")
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("DataSetEntry.created_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DataSetEntry.description required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DataSetEntry.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataSetEntry.name required")
    if "Origin" in data:
        out["origin"] = data["Origin"]
    else:
        raise DeserializationError("DataSetEntry.origin required")
    if "OriginDetails" in data:
        import aws_sdk_dataexchange.types.origin_details

        out["origin_details"] = (
            aws_sdk_dataexchange.types.origin_details.deserialize_json(
                data["OriginDetails"]
            )
        )
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("DataSetEntry.updated_at required")
    return out
