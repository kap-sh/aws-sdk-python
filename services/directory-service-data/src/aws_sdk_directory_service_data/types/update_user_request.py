"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_directory_service_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.attributes
    import aws_sdk_directory_service_data.types.client_token
    import aws_sdk_directory_service_data.types.directory_id
    import aws_sdk_directory_service_data.types.email_address
    import aws_sdk_directory_service_data.types.given_name
    import aws_sdk_directory_service_data.types.surname
    import aws_sdk_directory_service_data.types.update_type
    import aws_sdk_directory_service_data.types.user_name


class UpdateUserRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service_data.types.directory_id.DirectoryId"
    """<p> The identifier (ID) of the directory that's associated with the user. </p>"""
    sam_account_name: "aws_sdk_directory_service_data.types.user_name.UserName"
    """<p> The name of the user. </p>"""
    email_address: NotRequired[
        "aws_sdk_directory_service_data.types.email_address.EmailAddress"
    ]
    """<p> The email address of the user. </p>"""
    given_name: NotRequired["aws_sdk_directory_service_data.types.given_name.GivenName"]
    """<p> The first name of the user. </p>"""
    surname: NotRequired["aws_sdk_directory_service_data.types.surname.Surname"]
    """<p> The last name of the user. </p>"""
    other_attributes: NotRequired[
        "aws_sdk_directory_service_data.types.attributes.Attributes"
    ]
    r"""<p> An expression that defines one or more attribute names with the data type and value of each attribute. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see <a href=\"https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html\">Directory Service Data Attributes</a>. </p> <note> <p> Attribute names are case insensitive. </p> </note>"""
    update_type: NotRequired[
        "aws_sdk_directory_service_data.types.update_type.UpdateType"
    ]
    """<p> The type of update to be performed. If no value exists for the attribute, use <code>ADD</code>. Otherwise, use <code>REPLACE</code> to change an attribute value or <code>REMOVE</code> to clear the attribute value. </p>"""
    client_token: NotRequired[
        "aws_sdk_directory_service_data.types.client_token.ClientToken"
    ]
    """<p> A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call. </p> <p> A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours. </p> <p> If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an <code>ConflictException</code>. </p> <note> <p> This parameter is optional when using the CLI or SDK. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["SAMAccountName"] = value["sam_account_name"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "other_attributes" in value:
        import aws_sdk_directory_service_data.types.attributes

        out["OtherAttributes"] = (
            aws_sdk_directory_service_data.types.attributes.serialize_json(
                value["other_attributes"]
            )
        )
    if "update_type" in value:
        import aws_sdk_directory_service_data.types.update_type

        out["UpdateType"] = (
            aws_sdk_directory_service_data.types.update_type.serialize_json(
                value["update_type"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "SAMAccountName" in data:
        out["sam_account_name"] = data["SAMAccountName"]
    else:
        raise DeserializationError("UpdateUserRequest.sam_account_name required")
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "OtherAttributes" in data:
        import aws_sdk_directory_service_data.types.attributes

        out["other_attributes"] = (
            aws_sdk_directory_service_data.types.attributes.deserialize_json(
                data["OtherAttributes"]
            )
        )
    if "UpdateType" in data:
        import aws_sdk_directory_service_data.types.update_type

        out["update_type"] = (
            aws_sdk_directory_service_data.types.update_type.deserialize_json(
                data["UpdateType"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
