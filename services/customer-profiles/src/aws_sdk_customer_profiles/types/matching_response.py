"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.auto_merging
    import aws_sdk_customer_profiles.types.exporting_config
    import aws_sdk_customer_profiles.types.job_schedule
    import aws_sdk_customer_profiles.types.optional_boolean


class MatchingResponse(TypedDict, closed=True):
    enabled: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>The flag that enables the matching process of duplicate profiles.</p>"""
    job_schedule: NotRequired[
        "aws_sdk_customer_profiles.types.job_schedule.JobSchedule"
    ]
    """<p>The day and time when do you want to start the Identity Resolution Job every week.</p>"""
    auto_merging: NotRequired[
        "aws_sdk_customer_profiles.types.auto_merging.AutoMerging"
    ]
    """<p>Configuration information about the auto-merging process.</p>"""
    exporting_config: NotRequired[
        "aws_sdk_customer_profiles.types.exporting_config.ExportingConfig"
    ]
    """<p>Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "job_schedule" in value:
        import aws_sdk_customer_profiles.types.job_schedule

        out["JobSchedule"] = (
            aws_sdk_customer_profiles.types.job_schedule.serialize_json(
                value["job_schedule"]
            )
        )
    if "auto_merging" in value:
        import aws_sdk_customer_profiles.types.auto_merging

        out["AutoMerging"] = (
            aws_sdk_customer_profiles.types.auto_merging.serialize_json(
                value["auto_merging"]
            )
        )
    if "exporting_config" in value:
        import aws_sdk_customer_profiles.types.exporting_config

        out["ExportingConfig"] = (
            aws_sdk_customer_profiles.types.exporting_config.serialize_json(
                value["exporting_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatchingResponse:
    out: MatchingResponse = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "JobSchedule" in data:
        import aws_sdk_customer_profiles.types.job_schedule

        out["job_schedule"] = (
            aws_sdk_customer_profiles.types.job_schedule.deserialize_json(
                data["JobSchedule"]
            )
        )
    if "AutoMerging" in data:
        import aws_sdk_customer_profiles.types.auto_merging

        out["auto_merging"] = (
            aws_sdk_customer_profiles.types.auto_merging.deserialize_json(
                data["AutoMerging"]
            )
        )
    if "ExportingConfig" in data:
        import aws_sdk_customer_profiles.types.exporting_config

        out["exporting_config"] = (
            aws_sdk_customer_profiles.types.exporting_config.deserialize_json(
                data["ExportingConfig"]
            )
        )
    return out
