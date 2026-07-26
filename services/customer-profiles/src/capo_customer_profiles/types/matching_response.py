"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.auto_merging
    import capo_customer_profiles.types.exporting_config
    import capo_customer_profiles.types.job_schedule
    import capo_customer_profiles.types.optional_boolean


class MatchingResponse(TypedDict, closed=True):
    enabled: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>The flag that enables the matching process of duplicate profiles.</p>"""
    job_schedule: NotRequired["capo_customer_profiles.types.job_schedule.JobSchedule"]
    """<p>The day and time when do you want to start the Identity Resolution Job every week.</p>"""
    auto_merging: NotRequired["capo_customer_profiles.types.auto_merging.AutoMerging"]
    """<p>Configuration information about the auto-merging process.</p>"""
    exporting_config: NotRequired[
        "capo_customer_profiles.types.exporting_config.ExportingConfig"
    ]
    """<p>Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "job_schedule" in value:
        import capo_customer_profiles.types.job_schedule

        out["JobSchedule"] = capo_customer_profiles.types.job_schedule.serialize_json(
            value["job_schedule"]
        )
    if "auto_merging" in value:
        import capo_customer_profiles.types.auto_merging

        out["AutoMerging"] = capo_customer_profiles.types.auto_merging.serialize_json(
            value["auto_merging"]
        )
    if "exporting_config" in value:
        import capo_customer_profiles.types.exporting_config

        out["ExportingConfig"] = (
            capo_customer_profiles.types.exporting_config.serialize_json(
                value["exporting_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatchingResponse:
    out: MatchingResponse = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "JobSchedule" in data:
        import capo_customer_profiles.types.job_schedule

        out["job_schedule"] = (
            capo_customer_profiles.types.job_schedule.deserialize_json(
                data["JobSchedule"]
            )
        )
    if "AutoMerging" in data:
        import capo_customer_profiles.types.auto_merging

        out["auto_merging"] = (
            capo_customer_profiles.types.auto_merging.deserialize_json(
                data["AutoMerging"]
            )
        )
    if "ExportingConfig" in data:
        import capo_customer_profiles.types.exporting_config

        out["exporting_config"] = (
            capo_customer_profiles.types.exporting_config.deserialize_json(
                data["ExportingConfig"]
            )
        )
    return out
