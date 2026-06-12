"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetEntitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.entity_descriptions


class GetEntitiesResponse(TypedDict):
    descriptions: NotRequired[
        "aws_sdk_iotthingsgraph.types.entity_descriptions.EntityDescriptions"
    ]
    """<p>An array of descriptions for the specified entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitiesResponse) -> dict:
    out: dict = {}
    if "descriptions" in value:
        import aws_sdk_iotthingsgraph.types.entity_descriptions

        out["descriptions"] = (
            aws_sdk_iotthingsgraph.types.entity_descriptions.serialize_aws_json_1_1(
                value["descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitiesResponse:
    out: GetEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "descriptions" in data:
        import aws_sdk_iotthingsgraph.types.entity_descriptions

        out["descriptions"] = (
            aws_sdk_iotthingsgraph.types.entity_descriptions.deserialize_aws_json_1_1(
                data["descriptions"]
            )
        )
    return out
