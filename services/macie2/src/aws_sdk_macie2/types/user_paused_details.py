"""Generated from Smithy shape ``com.amazonaws.macie2#UserPausedDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601


class UserPausedDetails(TypedDict, closed=True):
    job_expires_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the job or job run will expire and be cancelled if you don't resume it first.</p>"""
    job_imminent_expiration_health_event_arn: NotRequired[
        "aws_sdk_macie2.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the Health event that Amazon Macie sent to notify you of the job or job run's pending expiration and cancellation. This value is null if a job has been paused for less than 23 days.</p>"""
    job_paused_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when you paused the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPausedDetails) -> dict:
    out: dict = {}
    if "job_expires_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["jobExpiresAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["job_expires_at"]
        )
    if "job_imminent_expiration_health_event_arn" in value:
        out["jobImminentExpirationHealthEventArn"] = value[
            "job_imminent_expiration_health_event_arn"
        ]
    if "job_paused_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["jobPausedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["job_paused_at"]
        )
    return out


def deserialize_json(data: dict) -> UserPausedDetails:
    out: UserPausedDetails = {}  # type: ignore[typeddict-item]
    if "jobExpiresAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["job_expires_at"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["jobExpiresAt"]
            )
        )
    if "jobImminentExpirationHealthEventArn" in data:
        out["job_imminent_expiration_health_event_arn"] = data[
            "jobImminentExpirationHealthEventArn"
        ]
    if "jobPausedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["job_paused_at"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["jobPausedAt"]
            )
        )
    return out
