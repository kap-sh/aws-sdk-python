"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEntityTypesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.entity_type_list
    import aws_sdk_frauddetector.types.string


class GetEntityTypesResult(TypedDict, closed=True):
    entity_types: NotRequired[
        "aws_sdk_frauddetector.types.entity_type_list.entityTypeList"
    ]
    """<p>An array of entity types.</p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntityTypesResult) -> dict:
    out: dict = {}
    if "entity_types" in value:
        import aws_sdk_frauddetector.types.entity_type_list

        out["entityTypes"] = (
            aws_sdk_frauddetector.types.entity_type_list.serialize_aws_json_1_1(
                value["entity_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntityTypesResult:
    out: GetEntityTypesResult = {}  # type: ignore[typeddict-item]
    if "entityTypes" in data:
        import aws_sdk_frauddetector.types.entity_type_list

        out["entity_types"] = (
            aws_sdk_frauddetector.types.entity_type_list.deserialize_aws_json_1_1(
                data["entityTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
