"""Generated from Smithy shape ``com.amazonaws.ecs#PutAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes


class PutAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>The attributes applied to your resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAttributesResponse:
    out: PutAttributesResponse = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    return out
