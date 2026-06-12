"""Generated from Smithy shape ``com.amazonaws.snowball#LongTermPricingListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.java_boolean
    import aws_sdk_snowball.types.job_id
    import aws_sdk_snowball.types.long_term_pricing_associated_job_id_list
    import aws_sdk_snowball.types.long_term_pricing_id
    import aws_sdk_snowball.types.long_term_pricing_type
    import aws_sdk_snowball.types.snowball_type
    import aws_sdk_snowball.types.string
    import aws_sdk_snowball.types.timestamp


class LongTermPricingListEntry(TypedDict):
    long_term_pricing_id: NotRequired[
        "aws_sdk_snowball.types.long_term_pricing_id.LongTermPricingId"
    ]
    """<p>The ID of the long-term pricing type for the device.</p>"""
    long_term_pricing_end_date: NotRequired[
        "aws_sdk_snowball.types.timestamp.Timestamp"
    ]
    """<p>The end date the long-term pricing contract.</p>"""
    long_term_pricing_start_date: NotRequired[
        "aws_sdk_snowball.types.timestamp.Timestamp"
    ]
    """<p>The start date of the long-term pricing contract.</p>"""
    long_term_pricing_type: NotRequired[
        "aws_sdk_snowball.types.long_term_pricing_type.LongTermPricingType"
    ]
    """<p>The type of long-term pricing that was selected for the device.</p>"""
    current_active_job: NotRequired["aws_sdk_snowball.types.job_id.JobId"]
    """<p>The current active jobs on the device the long-term pricing type.</p>"""
    replacement_job: NotRequired["aws_sdk_snowball.types.job_id.JobId"]
    """<p>A new device that replaces a device that is ordered with long-term pricing.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "aws_sdk_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>If set to <code>true</code>, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.</p>"""
    long_term_pricing_status: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The status of the long-term pricing type.</p>"""
    snowball_type: NotRequired["aws_sdk_snowball.types.snowball_type.SnowballType"]
    """<p>The type of Snow Family devices associated with this long-term pricing job.</p>"""
    job_ids: NotRequired[
        "aws_sdk_snowball.types.long_term_pricing_associated_job_id_list.LongTermPricingAssociatedJobIdList"
    ]
    """<p>The IDs of the jobs that are associated with a long-term pricing type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LongTermPricingListEntry) -> dict:
    out: dict = {}
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "long_term_pricing_end_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["LongTermPricingEndDate"] = (
            aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
                value["long_term_pricing_end_date"]
            )
        )
    if "long_term_pricing_start_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["LongTermPricingStartDate"] = (
            aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
                value["long_term_pricing_start_date"]
            )
        )
    if "long_term_pricing_type" in value:
        import aws_sdk_snowball.types.long_term_pricing_type

        out["LongTermPricingType"] = (
            aws_sdk_snowball.types.long_term_pricing_type.serialize_aws_json_1_1(
                value["long_term_pricing_type"]
            )
        )
    if "current_active_job" in value:
        out["CurrentActiveJob"] = value["current_active_job"]
    if "replacement_job" in value:
        out["ReplacementJob"] = value["replacement_job"]
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    if "long_term_pricing_status" in value:
        out["LongTermPricingStatus"] = value["long_term_pricing_status"]
    if "snowball_type" in value:
        import aws_sdk_snowball.types.snowball_type

        out["SnowballType"] = (
            aws_sdk_snowball.types.snowball_type.serialize_aws_json_1_1(
                value["snowball_type"]
            )
        )
    if "job_ids" in value:
        import aws_sdk_snowball.types.long_term_pricing_associated_job_id_list

        out["JobIds"] = (
            aws_sdk_snowball.types.long_term_pricing_associated_job_id_list.serialize_aws_json_1_1(
                value["job_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LongTermPricingListEntry:
    out: LongTermPricingListEntry = {}  # type: ignore[typeddict-item]
    if "LongTermPricingId" in data:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    if "LongTermPricingEndDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["long_term_pricing_end_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["LongTermPricingEndDate"]
            )
        )
    if "LongTermPricingStartDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["long_term_pricing_start_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["LongTermPricingStartDate"]
            )
        )
    if "LongTermPricingType" in data:
        import aws_sdk_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            aws_sdk_snowball.types.long_term_pricing_type.deserialize_aws_json_1_1(
                data["LongTermPricingType"]
            )
        )
    if "CurrentActiveJob" in data:
        out["current_active_job"] = data["CurrentActiveJob"]
    if "ReplacementJob" in data:
        out["replacement_job"] = data["ReplacementJob"]
    if "IsLongTermPricingAutoRenew" in data:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    if "LongTermPricingStatus" in data:
        out["long_term_pricing_status"] = data["LongTermPricingStatus"]
    if "SnowballType" in data:
        import aws_sdk_snowball.types.snowball_type

        out["snowball_type"] = (
            aws_sdk_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if "JobIds" in data:
        import aws_sdk_snowball.types.long_term_pricing_associated_job_id_list

        out["job_ids"] = (
            aws_sdk_snowball.types.long_term_pricing_associated_job_id_list.deserialize_aws_json_1_1(
                data["JobIds"]
            )
        )
    return out
