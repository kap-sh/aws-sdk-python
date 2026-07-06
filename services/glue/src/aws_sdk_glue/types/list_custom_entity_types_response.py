"""Generated from Smithy shape ``com.amazonaws.glue#ListCustomEntityTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.custom_entity_types
    import aws_sdk_glue.types.pagination_token


class ListCustomEntityTypesResponse(TypedDict, closed=True):
    custom_entity_types: NotRequired[
        "aws_sdk_glue.types.custom_entity_types.CustomEntityTypes"
    ]
    """<p>A list of <code>CustomEntityType</code> objects representing custom patterns.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomEntityTypesResponse) -> dict:
    out: dict = {}
    if "custom_entity_types" in value:
        import aws_sdk_glue.types.custom_entity_types

        out["CustomEntityTypes"] = (
            aws_sdk_glue.types.custom_entity_types.serialize_aws_json_1_1(
                value["custom_entity_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomEntityTypesResponse:
    out: ListCustomEntityTypesResponse = {}  # type: ignore[typeddict-item]
    if "CustomEntityTypes" in data:
        import aws_sdk_glue.types.custom_entity_types

        out["custom_entity_types"] = (
            aws_sdk_glue.types.custom_entity_types.deserialize_aws_json_1_1(
                data["CustomEntityTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
