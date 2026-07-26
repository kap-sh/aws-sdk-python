"""Generated from Smithy shape ``com.amazonaws.b2bi#EdiType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_b2bi.types.x12_details


class _EdiType_x12Details(TypedDict, closed=True):
    x12Details: "capo_b2bi.types.x12_details.X12Details"


EdiType: TypeAlias = _EdiType_x12Details


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EdiType) -> dict:
    if "x12Details" in value:
        import capo_b2bi.types.x12_details

        return {
            "x12Details": capo_b2bi.types.x12_details.serialize_aws_json_1_0(
                value["x12Details"]
            )
        }
    else:
        raise SerializationError("EdiType: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EdiType:
    if "x12Details" in data:
        import capo_b2bi.types.x12_details

        return {
            "x12Details": capo_b2bi.types.x12_details.deserialize_aws_json_1_0(
                data["x12Details"]
            )
        }
    else:
        raise DeserializationError("EdiType: no recognized variant key")
