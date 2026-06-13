"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonElasticsearchParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.domain


class AmazonElasticsearchParameters(TypedDict):
    domain: "aws_sdk_quicksight.types.domain.Domain"
    """<p>The OpenSearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonElasticsearchParameters) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> AmazonElasticsearchParameters:
    out: AmazonElasticsearchParameters = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("AmazonElasticsearchParameters.domain required")
    return out
