"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.device_list_type
    import aws_sdk_cognito_identity_provider.types.search_pagination_token_type


class ListDevicesResponse(TypedDict, closed=True):
    devices: NotRequired[
        "aws_sdk_cognito_identity_provider.types.device_list_type.DeviceListType"
    ]
    """<p>An array of devices and their details. Each entry that's returned includes device information, last-accessed and created dates, and the device key.</p>"""
    pagination_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.search_pagination_token_type.SearchPaginationTokenType"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesResponse) -> dict:
    out: dict = {}
    if "devices" in value:
        import aws_sdk_cognito_identity_provider.types.device_list_type

        out["Devices"] = (
            aws_sdk_cognito_identity_provider.types.device_list_type.serialize_aws_json_1_1(
                value["devices"]
            )
        )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesResponse:
    out: ListDevicesResponse = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import aws_sdk_cognito_identity_provider.types.device_list_type

        out["devices"] = (
            aws_sdk_cognito_identity_provider.types.device_list_type.deserialize_aws_json_1_1(
                data["Devices"]
            )
        )
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    return out
