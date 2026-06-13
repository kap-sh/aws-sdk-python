"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service


class UpdateServiceResponse(TypedDict):
    service: "aws_sdk_resiliencehubv2.types.service.Service"
    """<p>The updated service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service

    out["service"] = aws_sdk_resiliencehubv2.types.service.serialize_json(
        value["service"]
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_resiliencehubv2.types.service

        out["service"] = aws_sdk_resiliencehubv2.types.service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("UpdateServiceResponse.service required")
    return out
