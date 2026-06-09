"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes


class DeleteAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>A list of attribute objects that were successfully deleted from your resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAttributesResponse:
    out: DeleteAttributesResponse = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    return out
