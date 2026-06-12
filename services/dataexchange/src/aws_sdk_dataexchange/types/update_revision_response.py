"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateRevisionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__boolean
    import aws_sdk_dataexchange.types.__string_min0_max16384
    import aws_sdk_dataexchange.types.__string_min10_max512
    import aws_sdk_dataexchange.types.arn
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.timestamp


class UpdateRevisionResponse(TypedDict):
    arn: NotRequired["aws_sdk_dataexchange.types.arn.Arn"]
    """<p>The ARN for the revision.</p>"""
    comment: NotRequired[
        "aws_sdk_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
    ]
    """<p>An optional comment about the revision.</p>"""
    created_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the revision was created, in ISO 8601 format.</p>"""
    data_set_id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The unique identifier for the data set associated with the data set revision.</p>"""
    finalized: "aws_sdk_dataexchange.types.__boolean.__boolean"
    """<p>To publish a revision to a data set in a product, the revision must first be finalized. Finalizing a revision tells AWS Data Exchange that changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products. Finalized revisions can be published through the AWS Data Exchange console or the AWS Marketplace Catalog API, using the StartChangeSet AWS Marketplace Catalog API action. When using the API, revisions are uniquely identified by their ARN.</p>"""
    id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The unique identifier for the revision.</p>"""
    source_id: NotRequired["aws_sdk_dataexchange.types.id.Id"]
    """<p>The revision ID of the owned revision corresponding to the entitled revision being viewed. This parameter is returned when a revision owner is viewing the entitled copy of its owned revision.</p>"""
    updated_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the revision was last updated, in ISO 8601 format.</p>"""
    revocation_comment: NotRequired[
        "aws_sdk_dataexchange.types.__string_min10_max512.__stringMin10Max512"
    ]
    """<p>A required comment to inform subscribers of the reason their access to the revision was revoked.</p>"""
    revoked: "aws_sdk_dataexchange.types.__boolean.__boolean"
    """<p>A status indicating that subscribers' access to the revision was revoked.</p>"""
    revoked_at: NotRequired["aws_sdk_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the revision was revoked, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRevisionResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "created_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["CreatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    out["Finalized"] = value.get("finalized", False)
    if "id" in value:
        out["Id"] = value["id"]
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "updated_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["UpdatedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "revocation_comment" in value:
        out["RevocationComment"] = value["revocation_comment"]
    out["Revoked"] = value.get("revoked", False)
    if "revoked_at" in value:
        import aws_sdk_dataexchange.types.timestamp

        out["RevokedAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
            value["revoked_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRevisionResponse:
    out: UpdateRevisionResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "CreatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["created_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "Finalized" in data:
        out["finalized"] = data["Finalized"]
    else:
        out["finalized"] = False
    if "Id" in data:
        out["id"] = data["Id"]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    if "UpdatedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["updated_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "RevocationComment" in data:
        out["revocation_comment"] = data["RevocationComment"]
    if "Revoked" in data:
        out["revoked"] = data["Revoked"]
    else:
        out["revoked"] = False
    if "RevokedAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["revoked_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["RevokedAt"]
        )
    return out
