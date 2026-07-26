"""Generated from Smithy shape ``com.amazonaws.macie2#GetMacieSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601
    import capo_macie2.types.finding_publishing_frequency
    import capo_macie2.types.macie_status


class GetMacieSessionResponse(TypedDict, closed=True):
    created_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie account was created.</p>"""
    finding_publishing_frequency: NotRequired[
        "capo_macie2.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>The frequency with which Amazon Macie publishes updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).</p>"""
    service_role: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the service-linked role that allows Amazon Macie to monitor and analyze data in Amazon Web Services resources for the account.</p>"""
    status: NotRequired["capo_macie2.types.macie_status.MacieStatus"]
    """<p>The current status of the Amazon Macie account. Possible values are: PAUSED, the account is enabled but all Macie activities are suspended (paused) for the account; and, ENABLED, the account is enabled and all Macie activities are enabled for the account.</p>"""
    updated_at: NotRequired["capo_macie2.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status or configuration settings for the Amazon Macie account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMacieSessionResponse) -> dict:
    out: dict = {}
    if "created_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["createdAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "finding_publishing_frequency" in value:
        import capo_macie2.types.finding_publishing_frequency

        out["findingPublishingFrequency"] = (
            capo_macie2.types.finding_publishing_frequency.serialize_json(
                value["finding_publishing_frequency"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "status" in value:
        import capo_macie2.types.macie_status

        out["status"] = capo_macie2.types.macie_status.serialize_json(value["status"])
    if "updated_at" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["updatedAt"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetMacieSessionResponse:
    out: GetMacieSessionResponse = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["created_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "findingPublishingFrequency" in data:
        import capo_macie2.types.finding_publishing_frequency

        out["finding_publishing_frequency"] = (
            capo_macie2.types.finding_publishing_frequency.deserialize_json(
                data["findingPublishingFrequency"]
            )
        )
    if "serviceRole" in data:
        out["service_role"] = data["serviceRole"]
    if "status" in data:
        import capo_macie2.types.macie_status

        out["status"] = capo_macie2.types.macie_status.deserialize_json(data["status"])
    if "updatedAt" in data:
        import capo_macie2.types.__timestamp_iso8601

        out["updated_at"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["updatedAt"]
        )
    return out
