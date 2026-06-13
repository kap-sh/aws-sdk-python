"""Generated from Smithy shape ``com.amazonaws.quicksight#CredentialPair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source_parameters_list
    import aws_sdk_quicksight.types.db_username
    import aws_sdk_quicksight.types.password


class CredentialPair(TypedDict):
    username: "aws_sdk_quicksight.types.db_username.DbUsername"
    """<p>User name.</p>"""
    password: "aws_sdk_quicksight.types.password.Password"
    """<p>Password.</p>"""
    alternate_data_source_parameters: NotRequired[
        "aws_sdk_quicksight.types.data_source_parameters_list.DataSourceParametersList"
    ]
    """<p>A set of alternate data source parameters that you want to share for these credentials. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the <code>DataSourceParameters</code> structure that's in the request with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the <code>AlternateDataSourceParameters</code> list is null, the <code>DataSourceParameters</code> originally used with these <code>Credentials</code> is automatically allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialPair) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    if "alternate_data_source_parameters" in value:
        import aws_sdk_quicksight.types.data_source_parameters_list

        out["AlternateDataSourceParameters"] = (
            aws_sdk_quicksight.types.data_source_parameters_list.serialize_json(
                value["alternate_data_source_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CredentialPair:
    out: CredentialPair = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("CredentialPair.username required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CredentialPair.password required")
    if "AlternateDataSourceParameters" in data:
        import aws_sdk_quicksight.types.data_source_parameters_list

        out["alternate_data_source_parameters"] = (
            aws_sdk_quicksight.types.data_source_parameters_list.deserialize_json(
                data["AlternateDataSourceParameters"]
            )
        )
    return out
