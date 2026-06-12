"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class DeleteRecommenderSchemaRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_schema_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender schema to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommenderSchemaRequest:
    out: DeleteRecommenderSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
