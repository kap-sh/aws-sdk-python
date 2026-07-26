"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudsterRegistrationJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.fraudster_registration_job_summary

FraudsterRegistrationJobSummaries: TypeAlias = list[
    "capo_voice_id.types.fraudster_registration_job_summary.FraudsterRegistrationJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudsterRegistrationJobSummaries) -> list:
    import capo_voice_id.types.fraudster_registration_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_voice_id.types.fraudster_registration_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FraudsterRegistrationJobSummaries:
    import capo_voice_id.types.fraudster_registration_job_summary

    out: FraudsterRegistrationJobSummaries = []
    for item in data:
        out.append(
            capo_voice_id.types.fraudster_registration_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
