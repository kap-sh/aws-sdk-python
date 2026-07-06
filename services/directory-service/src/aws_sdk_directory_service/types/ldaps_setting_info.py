"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSSettingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.last_updated_date_time
    import aws_sdk_directory_service.types.ldaps_status
    import aws_sdk_directory_service.types.ldaps_status_reason


class LDAPSSettingInfo(TypedDict, closed=True):
    ldaps_status: NotRequired[
        "aws_sdk_directory_service.types.ldaps_status.LDAPSStatus"
    ]
    """<p>The state of the LDAPS settings.</p>"""
    ldaps_status_reason: NotRequired[
        "aws_sdk_directory_service.types.ldaps_status_reason.LDAPSStatusReason"
    ]
    """<p>Describes a state change for LDAPS.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the LDAPS settings were last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSSettingInfo) -> dict:
    out: dict = {}
    if "ldaps_status" in value:
        import aws_sdk_directory_service.types.ldaps_status

        out["LDAPSStatus"] = (
            aws_sdk_directory_service.types.ldaps_status.serialize_aws_json_1_1(
                value["ldaps_status"]
            )
        )
    if "ldaps_status_reason" in value:
        out["LDAPSStatusReason"] = value["ldaps_status_reason"]
    if "last_updated_date_time" in value:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            aws_sdk_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LDAPSSettingInfo:
    out: LDAPSSettingInfo = {}  # type: ignore[typeddict-item]
    if "LDAPSStatus" in data:
        import aws_sdk_directory_service.types.ldaps_status

        out["ldaps_status"] = (
            aws_sdk_directory_service.types.ldaps_status.deserialize_aws_json_1_1(
                data["LDAPSStatus"]
            )
        )
    if "LDAPSStatusReason" in data:
        out["ldaps_status_reason"] = data["LDAPSStatusReason"]
    if "LastUpdatedDateTime" in data:
        import aws_sdk_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            aws_sdk_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out
