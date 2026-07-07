"""Generated from Smithy shape ``com.amazonaws.health#OrganizationEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.account_id
    import aws_sdk_health.types.event
    import aws_sdk_health.types.event_description
    import aws_sdk_health.types.event_metadata


class OrganizationEventDetails(TypedDict, closed=True):
    aws_account_id: NotRequired["aws_sdk_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account numbers that contains the affected entities.</p>"""
    event: NotRequired["aws_sdk_health.types.event.Event"]
    event_description: NotRequired[
        "aws_sdk_health.types.event_description.EventDescription"
    ]
    event_metadata: NotRequired["aws_sdk_health.types.event_metadata.eventMetadata"]
    """<p>Additional metadata about the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationEventDetails) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "event" in value:
        import aws_sdk_health.types.event

        out["event"] = aws_sdk_health.types.event.serialize_aws_json_1_1(value["event"])
    if "event_description" in value:
        import aws_sdk_health.types.event_description

        out["eventDescription"] = (
            aws_sdk_health.types.event_description.serialize_aws_json_1_1(
                value["event_description"]
            )
        )
    if "event_metadata" in value:
        import aws_sdk_health.types.event_metadata

        out["eventMetadata"] = (
            aws_sdk_health.types.event_metadata.serialize_aws_json_1_1(
                value["event_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationEventDetails:
    out: OrganizationEventDetails = {}  # type: ignore[typeddict-item]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "event" in data:
        import aws_sdk_health.types.event

        out["event"] = aws_sdk_health.types.event.deserialize_aws_json_1_1(
            data["event"]
        )
    if "eventDescription" in data:
        import aws_sdk_health.types.event_description

        out["event_description"] = (
            aws_sdk_health.types.event_description.deserialize_aws_json_1_1(
                data["eventDescription"]
            )
        )
    if "eventMetadata" in data:
        import aws_sdk_health.types.event_metadata

        out["event_metadata"] = (
            aws_sdk_health.types.event_metadata.deserialize_aws_json_1_1(
                data["eventMetadata"]
            )
        )
    return out
