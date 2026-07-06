"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddressList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.address_list_arn
    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.address_list_name


class AddressList(TypedDict, closed=True):
    address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId"
    """<p>The identifier of the address list.</p>"""
    address_list_arn: "aws_sdk_mailmanager.types.address_list_arn.AddressListArn"
    """<p>The Amazon Resource Name (ARN) of the address list.</p>"""
    address_list_name: "aws_sdk_mailmanager.types.address_list_name.AddressListName"
    """<p>The user-friendly name of the address list.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address list was created.</p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address list was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddressList) -> dict:
    out: dict = {}
    out["AddressListId"] = value["address_list_id"]
    out["AddressListArn"] = value["address_list_arn"]
    out["AddressListName"] = value["address_list_name"]
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["LastUpdatedTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddressList:
    out: AddressList = {}  # type: ignore[typeddict-item]
    if "AddressListId" in data:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("AddressList.address_list_id required")
    if "AddressListArn" in data:
        out["address_list_arn"] = data["AddressListArn"]
    else:
        raise DeserializationError("AddressList.address_list_arn required")
    if "AddressListName" in data:
        out["address_list_name"] = data["AddressListName"]
    else:
        raise DeserializationError("AddressList.address_list_name required")
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("AddressList.created_timestamp required")
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("AddressList.last_updated_timestamp required")
    return out
