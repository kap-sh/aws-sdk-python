"""Generated from Smithy shape ``com.amazonaws.codeartifact#DomainDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.arn
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.domain_status
    import aws_sdk_codeartifact.types.integer
    import aws_sdk_codeartifact.types.long
    import aws_sdk_codeartifact.types.timestamp


class DomainDescription(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codeartifact.types.domain_name.DomainName"]
    """<p> The name of the domain. </p>"""
    owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID that owns the domain. </p>"""
    arn: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The Amazon Resource Name (ARN) of the domain. </p>"""
    status: NotRequired["aws_sdk_codeartifact.types.domain_status.DomainStatus"]
    """<p> The current status of a domain. </p>"""
    created_time: NotRequired["aws_sdk_codeartifact.types.timestamp.Timestamp"]
    """<p> A timestamp that represents the date and time the domain was created. </p>"""
    encryption_key: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The ARN of an Key Management Service (KMS) key associated with a domain. </p>"""
    repository_count: "aws_sdk_codeartifact.types.integer.Integer"
    """<p> The number of repositories in the domain. </p>"""
    asset_size_bytes: "aws_sdk_codeartifact.types.long.Long"
    """<p> The total size of all assets in the domain. </p>"""
    s3_bucket_arn: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket that is used to store package assets in the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDescription) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_codeartifact.types.domain_status

        out["status"] = aws_sdk_codeartifact.types.domain_status.serialize_json(
            value["status"]
        )
    if "created_time" in value:
        import aws_sdk_codeartifact.types.timestamp

        out["createdTime"] = aws_sdk_codeartifact.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    out["repositoryCount"] = value.get("repository_count", 0)
    out["assetSizeBytes"] = value.get("asset_size_bytes", 0)
    if "s3_bucket_arn" in value:
        out["s3BucketArn"] = value["s3_bucket_arn"]
    return out


def deserialize_json(data: dict) -> DomainDescription:
    out: DomainDescription = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_codeartifact.types.domain_status

        out["status"] = aws_sdk_codeartifact.types.domain_status.deserialize_json(
            data["status"]
        )
    if "createdTime" in data:
        import aws_sdk_codeartifact.types.timestamp

        out["created_time"] = aws_sdk_codeartifact.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    if "repositoryCount" in data:
        out["repository_count"] = data["repositoryCount"]
    else:
        out["repository_count"] = 0
    if "assetSizeBytes" in data:
        out["asset_size_bytes"] = data["assetSizeBytes"]
    else:
        out["asset_size_bytes"] = 0
    if "s3BucketArn" in data:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    return out
