"""Generated from Smithy shape ``com.amazonaws.vpclattice#DomainVerificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.domain_verification_arn
    import aws_sdk_vpc_lattice.types.domain_verification_id
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.timestamp
    import aws_sdk_vpc_lattice.types.txt_method_config
    import aws_sdk_vpc_lattice.types.verification_status


class DomainVerificationSummary(TypedDict, closed=True):
    id: "aws_sdk_vpc_lattice.types.domain_verification_id.DomainVerificationId"
    """<p> The ID of the domain verification. </p>"""
    arn: "aws_sdk_vpc_lattice.types.domain_verification_arn.DomainVerificationArn"
    """<p> The Amazon Resource Name (ARN) of the domain verification. </p>"""
    domain_name: "aws_sdk_vpc_lattice.types.domain_name.DomainName"
    """<p> The domain name being verified. </p>"""
    status: "aws_sdk_vpc_lattice.types.verification_status.VerificationStatus"
    """<p> The current status of the domain verification process. </p>"""
    txt_method_config: NotRequired[
        "aws_sdk_vpc_lattice.types.txt_method_config.TxtMethodConfig"
    ]
    """<p> The TXT record configuration used for domain verification. </p>"""
    created_at: "aws_sdk_vpc_lattice.types.timestamp.Timestamp"
    """<p> The date and time that the domain verification was created, in ISO-8601 format. </p>"""
    last_verified_time: NotRequired["aws_sdk_vpc_lattice.types.timestamp.Timestamp"]
    """<p> The date and time that the domain was last successfully verified, in ISO-8601 format. </p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p> The tags associated with the domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainVerificationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["domainName"] = value["domain_name"]
    out["status"] = value["status"]
    if "txt_method_config" in value:
        import aws_sdk_vpc_lattice.types.txt_method_config

        out["txtMethodConfig"] = (
            aws_sdk_vpc_lattice.types.txt_method_config.serialize_json(
                value["txt_method_config"]
            )
        )
    import aws_sdk_vpc_lattice.types.timestamp

    out["createdAt"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
        value["created_at"]
    )
    if "last_verified_time" in value:
        import aws_sdk_vpc_lattice.types.timestamp

        out["lastVerifiedTime"] = aws_sdk_vpc_lattice.types.timestamp.serialize_json(
            value["last_verified_time"]
        )
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DomainVerificationSummary:
    out: DomainVerificationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DomainVerificationSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DomainVerificationSummary.arn required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("DomainVerificationSummary.domain_name required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DomainVerificationSummary.status required")
    if "txtMethodConfig" in data:
        import aws_sdk_vpc_lattice.types.txt_method_config

        out["txt_method_config"] = (
            aws_sdk_vpc_lattice.types.txt_method_config.deserialize_json(
                data["txtMethodConfig"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["created_at"] = aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DomainVerificationSummary.created_at required")
    if "lastVerifiedTime" in data:
        import aws_sdk_vpc_lattice.types.timestamp

        out["last_verified_time"] = (
            aws_sdk_vpc_lattice.types.timestamp.deserialize_json(
                data["lastVerifiedTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
