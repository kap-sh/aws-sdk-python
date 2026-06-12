"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodPayload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.date_time
    import aws_sdk_partnercentral_channel.types.minimum_notice_days
    import aws_sdk_partnercentral_channel.types.note
    import aws_sdk_partnercentral_channel.types.program_management_account_identifier
    import aws_sdk_partnercentral_channel.types.service_period_type


class StartServicePeriodPayload(TypedDict):
    program_management_account_identifier: "aws_sdk_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
    """<p>The identifier of the program management account.</p>"""
    note: NotRequired["aws_sdk_partnercentral_channel.types.note.Note"]
    """<p>A note providing additional information about the service period.</p>"""
    service_period_type: (
        "aws_sdk_partnercentral_channel.types.service_period_type.ServicePeriodType"
    )
    """<p>The type of service period being started.</p>"""
    minimum_notice_days: NotRequired[
        "aws_sdk_partnercentral_channel.types.minimum_notice_days.MinimumNoticeDays"
    ]
    """<p>The minimum number of days notice required for changes.</p>"""
    end_date: NotRequired["aws_sdk_partnercentral_channel.types.date_time.DateTime"]
    """<p>The end date of the service period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartServicePeriodPayload) -> dict:
    out: dict = {}
    out["programManagementAccountIdentifier"] = value[
        "program_management_account_identifier"
    ]
    if "note" in value:
        out["note"] = value["note"]
    import aws_sdk_partnercentral_channel.types.service_period_type

    out["servicePeriodType"] = (
        aws_sdk_partnercentral_channel.types.service_period_type.serialize_aws_json_1_0(
            value["service_period_type"]
        )
    )
    if "minimum_notice_days" in value:
        out["minimumNoticeDays"] = value["minimum_notice_days"]
    if "end_date" in value:
        import aws_sdk_partnercentral_channel.types.date_time

        out["endDate"] = (
            aws_sdk_partnercentral_channel.types.date_time.serialize_aws_json_1_0(
                value["end_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartServicePeriodPayload:
    out: StartServicePeriodPayload = {}  # type: ignore[typeddict-item]
    if "programManagementAccountIdentifier" in data:
        out["program_management_account_identifier"] = data[
            "programManagementAccountIdentifier"
        ]
    else:
        raise DeserializationError(
            "StartServicePeriodPayload.program_management_account_identifier required"
        )
    if "note" in data:
        out["note"] = data["note"]
    if "servicePeriodType" in data:
        import aws_sdk_partnercentral_channel.types.service_period_type

        out["service_period_type"] = (
            aws_sdk_partnercentral_channel.types.service_period_type.deserialize_aws_json_1_0(
                data["servicePeriodType"]
            )
        )
    else:
        raise DeserializationError(
            "StartServicePeriodPayload.service_period_type required"
        )
    if "minimumNoticeDays" in data:
        out["minimum_notice_days"] = data["minimumNoticeDays"]
    if "endDate" in data:
        import aws_sdk_partnercentral_channel.types.date_time

        out["end_date"] = (
            aws_sdk_partnercentral_channel.types.date_time.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    return out
