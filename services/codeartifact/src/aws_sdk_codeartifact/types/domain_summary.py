"""Generated from Smithy shape ``com.amazonaws.codeartifact#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.account_id
    import aws_sdk_codeartifact.types.arn
    import aws_sdk_codeartifact.types.domain_name
    import aws_sdk_codeartifact.types.domain_status
    import aws_sdk_codeartifact.types.timestamp


class DomainSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codeartifact.types.domain_name.DomainName"]
    """<p> The name of the domain. </p>"""
    owner: NotRequired["aws_sdk_codeartifact.types.account_id.AccountId"]
    """<p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>"""
    arn: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The ARN of the domain. </p>"""
    status: NotRequired["aws_sdk_codeartifact.types.domain_status.DomainStatus"]
    """<p> A string that contains the status of the domain. </p>"""
    created_time: NotRequired["aws_sdk_codeartifact.types.timestamp.Timestamp"]
    """<p> A timestamp that contains the date and time the domain was created. </p>"""
    encryption_key: NotRequired["aws_sdk_codeartifact.types.arn.Arn"]
    """<p> The key used to encrypt the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
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
    return out
