"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UserSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.given_name
    import aws_sdk_directory_service_data.types.sid
    import aws_sdk_directory_service_data.types.surname
    import aws_sdk_directory_service_data.types.user_name


class UserSummary(TypedDict):
    sid: "aws_sdk_directory_service_data.types.sid.SID"
    """<p> The unique security identifier (SID) of the user.</p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.user_name.UserName"
    """<p>The name of the user.</p>"""
    given_name: NotRequired["aws_sdk_directory_service_data.types.given_name.GivenName"]
    """<p>The first name of the user. </p>"""
    surname: NotRequired["aws_sdk_directory_service_data.types.surname.Surname"]
    """<p>The last name of the user.</p>"""
    enabled: "bool"
    """<p>Indicates whether the user account is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSummary) -> dict:
    out: dict = {}
    out["SID"] = value["sid"]
    out["SAMAccountName"] = value["sam_account_name"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> UserSummary:
    out: UserSummary = {}  # type: ignore[typeddict-item]
    if "SID" in data:
        out["sid"] = data["SID"]
    else:
        raise DeserializationError("UserSummary.sid required")
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("UserSummary.sam_account_name required")
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("UserSummary.enabled required")
    return out
