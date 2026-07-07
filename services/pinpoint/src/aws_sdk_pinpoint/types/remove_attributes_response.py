"""Generated from Smithy shape ``com.amazonaws.pinpoint#RemoveAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.attributes_resource


class RemoveAttributesResponse(TypedDict, closed=True):
    attributes_resource: NotRequired[
        "aws_sdk_pinpoint.types.attributes_resource.AttributesResource"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAttributesResponse) -> dict:
    out: dict = {}
    if "attributes_resource" in value:
        import aws_sdk_pinpoint.types.attributes_resource

        out["AttributesResource"] = (
            aws_sdk_pinpoint.types.attributes_resource.serialize_json(
                value["attributes_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> RemoveAttributesResponse:
    out: RemoveAttributesResponse = {}  # type: ignore[typeddict-item]
    if "AttributesResource" in data:
        import aws_sdk_pinpoint.types.attributes_resource

        out["attributes_resource"] = (
            aws_sdk_pinpoint.types.attributes_resource.deserialize_json(
                data["AttributesResource"]
            )
        )
    return out
