"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportAppResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.service


class ImportAppResponse(TypedDict):
    service: "aws_sdk_resiliencehubv2.types.service.Service"
    """<p>The imported service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAppResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.service

    out["service"] = aws_sdk_resiliencehubv2.types.service.serialize_json(
        value["service"]
    )
    return out


def deserialize_json(data: dict) -> ImportAppResponse:
    out: ImportAppResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_resiliencehubv2.types.service

        out["service"] = aws_sdk_resiliencehubv2.types.service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("ImportAppResponse.service required")
    return out
