"""Generated from Smithy shape ``com.amazonaws.securityhub#RelatedFinding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class RelatedFinding(TypedDict):
    product_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the product that generated a related finding.</p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The product-generated identifier for a related finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFinding) -> dict:
    out: dict = {}
    if "product_arn" in value:
        out["ProductArn"] = value["product_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> RelatedFinding:
    out: RelatedFinding = {}  # type: ignore[typeddict-item]
    if "ProductArn" in data:
        out["product_arn"] = data["ProductArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
