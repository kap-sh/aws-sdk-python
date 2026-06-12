"""Generated from Smithy shape ``com.amazonaws.appconfig#BadRequestDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_appconfig.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.invalid_configuration_detail_list


class _BadRequestDetails_InvalidConfiguration(TypedDict):
    InvalidConfiguration: "aws_sdk_appconfig.types.invalid_configuration_detail_list.InvalidConfigurationDetailList"


BadRequestDetails: TypeAlias = _BadRequestDetails_InvalidConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestDetails) -> dict:
    if "InvalidConfiguration" in value:
        import aws_sdk_appconfig.types.invalid_configuration_detail_list

        return {
            "InvalidConfiguration": aws_sdk_appconfig.types.invalid_configuration_detail_list.serialize_json(
                value["InvalidConfiguration"]
            )
        }
    else:
        raise SerializationError("BadRequestDetails: no variant present")


def deserialize_json(data: dict) -> BadRequestDetails:
    if "InvalidConfiguration" in data:
        import aws_sdk_appconfig.types.invalid_configuration_detail_list

        return {
            "InvalidConfiguration": aws_sdk_appconfig.types.invalid_configuration_detail_list.deserialize_json(
                data["InvalidConfiguration"]
            )
        }
    else:
        raise DeserializationError("BadRequestDetails: no recognized variant key")
