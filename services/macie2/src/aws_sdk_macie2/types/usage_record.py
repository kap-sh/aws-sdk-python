"""Generated from Smithy shape ``com.amazonaws.macie2#UsageRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_usage_by_account
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601


class UsageRecord(TypedDict):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that the data applies to.</p>"""
    automated_discovery_free_trial_start_date: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the free trial of automated sensitive data discovery started for the account. This value is null if automated sensitive data discovery hasn't been enabled for the account.</p>"""
    free_trial_start_date: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie free trial started for the account.</p>"""
    usage: NotRequired[
        "aws_sdk_macie2.types.__list_of_usage_by_account.__listOfUsageByAccount"
    ]
    """<p>An array of objects that contains usage data and quotas for the account. Each object contains the data for a specific usage metric and the corresponding quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageRecord) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "automated_discovery_free_trial_start_date" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["automatedDiscoveryFreeTrialStartDate"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
                value["automated_discovery_free_trial_start_date"]
            )
        )
    if "free_trial_start_date" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["freeTrialStartDate"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
                value["free_trial_start_date"]
            )
        )
    if "usage" in value:
        import aws_sdk_macie2.types.__list_of_usage_by_account

        out["usage"] = aws_sdk_macie2.types.__list_of_usage_by_account.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> UsageRecord:
    out: UsageRecord = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "automatedDiscoveryFreeTrialStartDate" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["automated_discovery_free_trial_start_date"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["automatedDiscoveryFreeTrialStartDate"]
            )
        )
    if "freeTrialStartDate" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["free_trial_start_date"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["freeTrialStartDate"]
            )
        )
    if "usage" in data:
        import aws_sdk_macie2.types.__list_of_usage_by_account

        out["usage"] = aws_sdk_macie2.types.__list_of_usage_by_account.deserialize_json(
            data["usage"]
        )
    return out
