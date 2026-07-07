"""Generated from Smithy shape ``com.amazonaws.appconfigdata#BadRequestDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_appconfigdata.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.invalid_parameter_map


class _BadRequestDetails_InvalidParameters(TypedDict, closed=True):
    InvalidParameters: (
        "aws_sdk_appconfigdata.types.invalid_parameter_map.InvalidParameterMap"
    )


BadRequestDetails: TypeAlias = _BadRequestDetails_InvalidParameters


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestDetails) -> dict:
    if "InvalidParameters" in value:
        import aws_sdk_appconfigdata.types.invalid_parameter_map

        return {
            "InvalidParameters": aws_sdk_appconfigdata.types.invalid_parameter_map.serialize_json(
                value["InvalidParameters"]
            )
        }
    else:
        raise SerializationError("BadRequestDetails: no variant present")


def deserialize_json(data: dict) -> BadRequestDetails:
    if "InvalidParameters" in data:
        import aws_sdk_appconfigdata.types.invalid_parameter_map

        return {
            "InvalidParameters": aws_sdk_appconfigdata.types.invalid_parameter_map.deserialize_json(
                data["InvalidParameters"]
            )
        }
    else:
        raise DeserializationError("BadRequestDetails: no recognized variant key")
