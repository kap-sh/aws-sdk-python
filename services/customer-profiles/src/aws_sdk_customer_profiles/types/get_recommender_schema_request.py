"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetRecommenderSchemaRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_schema_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender schema to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommenderSchemaRequest:
    out: GetRecommenderSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
