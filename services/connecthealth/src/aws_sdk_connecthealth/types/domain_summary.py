"""Generated from Smithy shape ``com.amazonaws.connecthealth#DomainSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_connecthealth.types.domain_arn
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.domain_name
    import aws_sdk_connecthealth.types.domain_status


class DomainSummary(TypedDict):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the Domain.</p>"""
    arn: "aws_sdk_connecthealth.types.domain_arn.DomainArn"
    """<p/>"""
    name: "aws_sdk_connecthealth.types.domain_name.DomainName"
    """<p/>"""
    status: "aws_sdk_connecthealth.types.domain_status.DomainStatus"
    """<p/>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the Domain was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import aws_sdk_connecthealth.types.domain_status

    out["status"] = aws_sdk_connecthealth.types.domain_status.serialize_json(
        value["status"]
    )
    import aws_sdk_connecthealth.types._prelude.timestamp

    out["createdAt"] = aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DomainSummary.domain_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DomainSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DomainSummary.name required")
    if "status" in data:
        import aws_sdk_connecthealth.types.domain_status

        out["status"] = aws_sdk_connecthealth.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DomainSummary.status required")
    if "createdAt" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DomainSummary.created_at required")
    return out
