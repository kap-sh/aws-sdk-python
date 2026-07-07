"""Generated from Smithy shape ``com.amazonaws.macie2#EnableMacieRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.finding_publishing_frequency
    import aws_sdk_macie2.types.macie_status


class EnableMacieRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    finding_publishing_frequency: NotRequired[
        "aws_sdk_macie2.types.finding_publishing_frequency.FindingPublishingFrequency"
    ]
    """<p>Specifies how often to publish updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).</p>"""
    status: NotRequired["aws_sdk_macie2.types.macie_status.MacieStatus"]
    """<p>Specifies the new status for the account. To enable Amazon Macie and start all Macie activities for the account, set this value to ENABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableMacieRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "finding_publishing_frequency" in value:
        import aws_sdk_macie2.types.finding_publishing_frequency

        out["findingPublishingFrequency"] = (
            aws_sdk_macie2.types.finding_publishing_frequency.serialize_json(
                value["finding_publishing_frequency"]
            )
        )
    if "status" in value:
        import aws_sdk_macie2.types.macie_status

        out["status"] = aws_sdk_macie2.types.macie_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> EnableMacieRequest:
    out: EnableMacieRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "findingPublishingFrequency" in data:
        import aws_sdk_macie2.types.finding_publishing_frequency

        out["finding_publishing_frequency"] = (
            aws_sdk_macie2.types.finding_publishing_frequency.deserialize_json(
                data["findingPublishingFrequency"]
            )
        )
    if "status" in data:
        import aws_sdk_macie2.types.macie_status

        out["status"] = aws_sdk_macie2.types.macie_status.deserialize_json(
            data["status"]
        )
    return out
