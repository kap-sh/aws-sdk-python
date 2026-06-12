"""Generated from Smithy shape ``com.amazonaws.voiceid#DomainSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.arn
    import aws_sdk_voice_id.types.description
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.domain_name
    import aws_sdk_voice_id.types.domain_status
    import aws_sdk_voice_id.types.server_side_encryption_configuration
    import aws_sdk_voice_id.types.server_side_encryption_update_details
    import aws_sdk_voice_id.types.timestamp
    import aws_sdk_voice_id.types.watchlist_details


class DomainSummary(TypedDict):
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain.</p>"""
    arn: NotRequired["aws_sdk_voice_id.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the domain.</p>"""
    name: NotRequired["aws_sdk_voice_id.types.domain_name.DomainName"]
    """<p>The client-provided name for the domain.</p>"""
    description: NotRequired["aws_sdk_voice_id.types.description.Description"]
    """<p>The description of the domain.</p>"""
    domain_status: NotRequired["aws_sdk_voice_id.types.domain_status.DomainStatus"]
    """<p>The current status of the domain.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_voice_id.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the domain was created.</p>"""
    updated_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the domain was last updated.</p>"""
    server_side_encryption_update_details: NotRequired[
        "aws_sdk_voice_id.types.server_side_encryption_update_details.ServerSideEncryptionUpdateDetails"
    ]
    """<p>Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domain's data can only be accessed using the new KMS key.</p>"""
    watchlist_details: NotRequired[
        "aws_sdk_voice_id.types.watchlist_details.WatchlistDetails"
    ]
    """<p>Provides information about <code>watchlistDetails</code> and <code>DefaultWatchlistID</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "domain_status" in value:
        out["DomainStatus"] = value["domain_status"]
    if "server_side_encryption_configuration" in value:
        import aws_sdk_voice_id.types.server_side_encryption_configuration

        out["ServerSideEncryptionConfiguration"] = (
            aws_sdk_voice_id.types.server_side_encryption_configuration.serialize_aws_json_1_0(
                value["server_side_encryption_configuration"]
            )
        )
    if "created_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["CreatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["UpdatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "server_side_encryption_update_details" in value:
        import aws_sdk_voice_id.types.server_side_encryption_update_details

        out["ServerSideEncryptionUpdateDetails"] = (
            aws_sdk_voice_id.types.server_side_encryption_update_details.serialize_aws_json_1_0(
                value["server_side_encryption_update_details"]
            )
        )
    if "watchlist_details" in value:
        import aws_sdk_voice_id.types.watchlist_details

        out["WatchlistDetails"] = (
            aws_sdk_voice_id.types.watchlist_details.serialize_aws_json_1_0(
                value["watchlist_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DomainStatus" in data:
        out["domain_status"] = data["DomainStatus"]
    if "ServerSideEncryptionConfiguration" in data:
        import aws_sdk_voice_id.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_voice_id.types.server_side_encryption_configuration.deserialize_aws_json_1_0(
                data["ServerSideEncryptionConfiguration"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["created_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["updated_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if "ServerSideEncryptionUpdateDetails" in data:
        import aws_sdk_voice_id.types.server_side_encryption_update_details

        out["server_side_encryption_update_details"] = (
            aws_sdk_voice_id.types.server_side_encryption_update_details.deserialize_aws_json_1_0(
                data["ServerSideEncryptionUpdateDetails"]
            )
        )
    if "WatchlistDetails" in data:
        import aws_sdk_voice_id.types.watchlist_details

        out["watchlist_details"] = (
            aws_sdk_voice_id.types.watchlist_details.deserialize_aws_json_1_0(
                data["WatchlistDetails"]
            )
        )
    return out
