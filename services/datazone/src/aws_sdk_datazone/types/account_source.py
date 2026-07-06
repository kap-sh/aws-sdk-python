"""Generated from Smithy shape ``com.amazonaws.datazone#AccountSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.account_info_list
    import aws_sdk_datazone.types.custom_account_pool_handler


class _AccountSource_accounts(TypedDict, closed=True):
    accounts: "aws_sdk_datazone.types.account_info_list.AccountInfoList"


class _AccountSource_customAccountPoolHandler(TypedDict, closed=True):
    customAccountPoolHandler: (
        "aws_sdk_datazone.types.custom_account_pool_handler.CustomAccountPoolHandler"
    )


AccountSource: TypeAlias = (
    _AccountSource_accounts | _AccountSource_customAccountPoolHandler
)


# --- restJson1 ser/de ---
def serialize_json(value: AccountSource) -> dict:
    if "accounts" in value:
        import aws_sdk_datazone.types.account_info_list

        return {
            "accounts": aws_sdk_datazone.types.account_info_list.serialize_json(
                value["accounts"]
            )
        }
    elif "customAccountPoolHandler" in value:
        import aws_sdk_datazone.types.custom_account_pool_handler

        return {
            "customAccountPoolHandler": aws_sdk_datazone.types.custom_account_pool_handler.serialize_json(
                value["customAccountPoolHandler"]
            )
        }
    else:
        raise SerializationError("AccountSource: no variant present")


def deserialize_json(data: dict) -> AccountSource:
    if "accounts" in data:
        import aws_sdk_datazone.types.account_info_list

        return {
            "accounts": aws_sdk_datazone.types.account_info_list.deserialize_json(
                data["accounts"]
            )
        }
    elif "customAccountPoolHandler" in data:
        import aws_sdk_datazone.types.custom_account_pool_handler

        return {
            "customAccountPoolHandler": aws_sdk_datazone.types.custom_account_pool_handler.deserialize_json(
                data["customAccountPoolHandler"]
            )
        }
    else:
        raise DeserializationError("AccountSource: no recognized variant key")
