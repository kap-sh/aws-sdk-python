"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableImportFindingsForProductRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class DisableImportFindingsForProductRequest(TypedDict, closed=True):
    product_subscription_arn: (
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    )
    """<p>The ARN of the integrated product to disable the integration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableImportFindingsForProductRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableImportFindingsForProductRequest:
    out: DisableImportFindingsForProductRequest = {}  # type: ignore[typeddict-item]
    return out
