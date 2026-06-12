"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RevokeServicePeriodHandshakeDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.date_time
    import aws_sdk_partnercentral_channel.types.minimum_notice_days
    import aws_sdk_partnercentral_channel.types.note
    import aws_sdk_partnercentral_channel.types.service_period_type


class RevokeServicePeriodHandshakeDetail(TypedDict):
    note: NotRequired["aws_sdk_partnercentral_channel.types.note.Note"]
    """<p>A note explaining the reason for revoking the service period.</p>"""
    service_period_type: NotRequired[
        "aws_sdk_partnercentral_channel.types.service_period_type.ServicePeriodType"
    ]
    """<p>The type of service period being revoked.</p>"""
    minimum_notice_days: NotRequired[
        "aws_sdk_partnercentral_channel.types.minimum_notice_days.MinimumNoticeDays"
    ]
    """<p>The minimum number of days notice required for revocation.</p>"""
    start_date: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The start date of the service period being revoked.</p>"""
    end_date: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The end date of the service period being revoked.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevokeServicePeriodHandshakeDetail) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    if "service_period_type" in value:
        import aws_sdk_partnercentral_channel.types.service_period_type

        out["servicePeriodType"] = (
            aws_sdk_partnercentral_channel.types.service_period_type.serialize_aws_json_1_0(
                value["service_period_type"]
            )
        )
    if "minimum_notice_days" in value:
        out["minimumNoticeDays"] = value["minimum_notice_days"]
    if "start_date" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["startDate"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["start_date"]
            )
        )
    if "end_date" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["endDate"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["end_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RevokeServicePeriodHandshakeDetail:
    out: RevokeServicePeriodHandshakeDetail = {}  # type: ignore[typeddict-item]
    if "note" in data:
        out["note"] = data["note"]
    if "servicePeriodType" in data:
        import aws_sdk_partnercentral_channel.types.service_period_type

        out["service_period_type"] = (
            aws_sdk_partnercentral_channel.types.service_period_type.deserialize_aws_json_1_0(
                data["servicePeriodType"]
            )
        )
    if "minimumNoticeDays" in data:
        out["minimum_notice_days"] = data["minimumNoticeDays"]
    if "startDate" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["start_date"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    if "endDate" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["end_date"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    return out
