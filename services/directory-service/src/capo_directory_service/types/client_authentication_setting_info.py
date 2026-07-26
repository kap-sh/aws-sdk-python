"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationSettingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.client_authentication_status
    import capo_directory_service.types.client_authentication_type
    import capo_directory_service.types.last_updated_date_time


class ClientAuthenticationSettingInfo(TypedDict, closed=True):
    type: NotRequired[
        "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
    ]
    """<p>The type of client authentication for the specified directory. If no type is specified, a list of all client authentication types that are supported for the directory is retrieved. </p>"""
    status: NotRequired[
        "capo_directory_service.types.client_authentication_status.ClientAuthenticationStatus"
    ]
    """<p>Whether the client authentication type is enabled or disabled for the specified directory.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the status of the client authentication type was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationSettingInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_directory_service.types.client_authentication_type

        out["Type"] = (
            capo_directory_service.types.client_authentication_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import capo_directory_service.types.client_authentication_status

        out["Status"] = (
            capo_directory_service.types.client_authentication_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientAuthenticationSettingInfo:
    out: ClientAuthenticationSettingInfo = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_directory_service.types.client_authentication_type

        out["type"] = (
            capo_directory_service.types.client_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Status" in data:
        import capo_directory_service.types.client_authentication_status

        out["status"] = (
            capo_directory_service.types.client_authentication_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastUpdatedDateTime" in data:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out
