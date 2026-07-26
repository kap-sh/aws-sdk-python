"""Generated from Smithy shape ``com.amazonaws.macie2#UpdateMacieSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.finding_publishing_frequency
    import capo_macie2.types.macie_status


class UpdateMacieSessionRequest(TypedDict, closed=True):
    finding_publishing_frequency: NotRequired[
        "capo_macie2.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>Specifies how often to publish updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).</p>"""
    status: NotRequired["capo_macie2.types.macie_status.MacieStatus"]
    """<p>Specifies a new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMacieSessionRequest) -> dict:
    out: dict = {}
    if "finding_publishing_frequency" in value:
        import capo_macie2.types.finding_publishing_frequency

        out["findingPublishingFrequency"] = (
            capo_macie2.types.finding_publishing_frequency.serialize_json(
                value["finding_publishing_frequency"]
            )
        )
    if "status" in value:
        import capo_macie2.types.macie_status

        out["status"] = capo_macie2.types.macie_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> UpdateMacieSessionRequest:
    out: UpdateMacieSessionRequest = {}  # type: ignore[typeddict-item]
    if "findingPublishingFrequency" in data:
        import capo_macie2.types.finding_publishing_frequency

        out["finding_publishing_frequency"] = (
            capo_macie2.types.finding_publishing_frequency.deserialize_json(
                data["findingPublishingFrequency"]
            )
        )
    if "status" in data:
        import capo_macie2.types.macie_status

        out["status"] = capo_macie2.types.macie_status.deserialize_json(data["status"])
    return out
