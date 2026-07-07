"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableImportFindingsForProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class EnableImportFindingsForProductRequest(TypedDict, closed=True):
    product_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the product to enable the integration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableImportFindingsForProductRequest) -> dict:
    out: dict = {}
    if "product_arn" in value:
        out["ProductArn"] = value["product_arn"]
    return out


def deserialize_json(data: dict) -> EnableImportFindingsForProductRequest:
    out: EnableImportFindingsForProductRequest = {}  # type: ignore[typeddict-item]
    if "ProductArn" in data:
        out["product_arn"] = data["ProductArn"]
    return out
