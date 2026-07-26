"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetAddressListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.address_list_arn
    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.address_list_name


class GetAddressListResponse(TypedDict, closed=True):
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of the address list resource.</p>"""
    address_list_arn: "capo_mailmanager.types.address_list_arn.AddressListArn"
    """<p>The Amazon Resource Name (ARN) of the address list resource.</p>"""
    address_list_name: "capo_mailmanager.types.address_list_name.AddressListName"
    """<p>A user-friendly name for the address list resource.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The date of when then address list was created.</p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The date of when the address list was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAddressListResponse) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    out["AddressListArn"] = value["address_list_arn"]
    out["AddressListName"] = value["address_list_name"]
    import capo_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    import capo_mailmanager.types._prelude.timestamp

    out["LastUpdatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAddressListResponse:
    out: GetAddressListResponse = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("GetAddressListResponse.address_list_id required")
    if "AddressListArn" in data:
        out["address_list_arn"] = data["AddressListArn"]
    else:
        raise DeserializationError("GetAddressListResponse.address_list_arn required")
    if "AddressListName" in data:
        out["address_list_name"] = data["AddressListName"]
    else:
        raise DeserializationError("GetAddressListResponse.address_list_name required")
    if "CreatedTimestamp" in data:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("GetAddressListResponse.created_timestamp required")
    if "LastUpdatedTimestamp" in data:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetAddressListResponse.last_updated_timestamp required"
        )
    return out
