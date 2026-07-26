"""Generated from Smithy shape ``com.amazonaws.connecthealth#DeleteDomainOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_arn
    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.domain_status


class DeleteDomainOutput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The id of the Domain requested for deletion</p>"""
    arn: "capo_connecthealth.types.domain_arn.DomainArn"
    """<p>The ARN of the Domain that was requested for deletion</p>"""
    status: "capo_connecthealth.types.domain_status.DomainStatus"
    """<p>Current status of Domain</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["arn"] = value["arn"]
    import capo_connecthealth.types.domain_status

    out["status"] = capo_connecthealth.types.domain_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDomainOutput:
    out: DeleteDomainOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DeleteDomainOutput.domain_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteDomainOutput.arn required")
    if "status" in data:
        import capo_connecthealth.types.domain_status

        out["status"] = capo_connecthealth.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteDomainOutput.status required")
    return out
