"""Generated from Smithy shape ``com.amazonaws.b2bi#OutboundEdiOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_b2bi.types.x12_envelope


class _OutboundEdiOptions_x12(TypedDict, closed=True):
    x12: "capo_b2bi.types.x12_envelope.X12Envelope"


OutboundEdiOptions: TypeAlias = _OutboundEdiOptions_x12


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutboundEdiOptions) -> dict:
    if "x12" in value:
        import capo_b2bi.types.x12_envelope

        return {
            "x12": capo_b2bi.types.x12_envelope.serialize_aws_json_1_0(value["x12"])
        }
    else:
        raise SerializationError("OutboundEdiOptions: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OutboundEdiOptions:
    if "x12" in data:
        import capo_b2bi.types.x12_envelope

        return {
            "x12": capo_b2bi.types.x12_envelope.deserialize_aws_json_1_0(data["x12"])
        }
    else:
        raise DeserializationError("OutboundEdiOptions: no recognized variant key")
