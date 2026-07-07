"""Generated from Smithy shape ``com.amazonaws.glacier#PurchaseProvisionedCapacityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class PurchaseProvisionedCapacityInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseProvisionedCapacityInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PurchaseProvisionedCapacityInput:
    out: PurchaseProvisionedCapacityInput = {}  # type: ignore[typeddict-item]
    return out
