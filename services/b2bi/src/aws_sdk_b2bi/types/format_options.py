"""Generated from Smithy shape ``com.amazonaws.b2bi#FormatOptions``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_details


class _FormatOptions_x12(TypedDict):
    x12: "aws_sdk_b2bi.types.x12_details.X12Details"


FormatOptions: TypeAlias = _FormatOptions_x12


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FormatOptions) -> dict:
    if "x12" in value:
        import aws_sdk_b2bi.types.x12_details

        return {
            "x12": aws_sdk_b2bi.types.x12_details.serialize_aws_json_1_0(value["x12"])
        }
    else:
        raise SerializationError("FormatOptions: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FormatOptions:
    if "x12" in data:
        import aws_sdk_b2bi.types.x12_details

        return {
            "x12": aws_sdk_b2bi.types.x12_details.deserialize_aws_json_1_0(data["x12"])
        }
    else:
        raise DeserializationError("FormatOptions: no recognized variant key")
