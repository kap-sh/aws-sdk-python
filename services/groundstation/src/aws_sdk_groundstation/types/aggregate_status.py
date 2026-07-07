"""Generated from Smithy shape ``com.amazonaws.groundstation#AggregateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_status
    import aws_sdk_groundstation.types.signature_map


class AggregateStatus(TypedDict, closed=True):
    status: "aws_sdk_groundstation.types.agent_status.AgentStatus"
    """<p>Aggregate status.</p>"""
    signature_map: NotRequired["aws_sdk_groundstation.types.signature_map.SignatureMap"]
    """<p>Sparse map of failure signatures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregateStatus) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.agent_status

    out["status"] = aws_sdk_groundstation.types.agent_status.serialize_json(
        value["status"]
    )
    if "signature_map" in value:
        import aws_sdk_groundstation.types.signature_map

        out["signatureMap"] = aws_sdk_groundstation.types.signature_map.serialize_json(
            value["signature_map"]
        )
    return out


def deserialize_json(data: dict) -> AggregateStatus:
    out: AggregateStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_groundstation.types.agent_status

        out["status"] = aws_sdk_groundstation.types.agent_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AggregateStatus.status required")
    if "signatureMap" in data:
        import aws_sdk_groundstation.types.signature_map

        out["signature_map"] = (
            aws_sdk_groundstation.types.signature_map.deserialize_json(
                data["signatureMap"]
            )
        )
    return out
