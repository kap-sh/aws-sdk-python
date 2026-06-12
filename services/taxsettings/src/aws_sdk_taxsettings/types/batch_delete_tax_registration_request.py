"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_ids

class BatchDeleteTaxRegistrationRequest(TypedDict):
    account_ids: "aws_sdk_taxsettings.types.account_ids.AccountIds"
    """<p>List of unique account identifiers. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.account_ids
    out["accountIds"] = aws_sdk_taxsettings.types.account_ids.serialize_json(value["account_ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteTaxRegistrationRequest:
    out: BatchDeleteTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_taxsettings.types.account_ids
        out["account_ids"] = aws_sdk_taxsettings.types.account_ids.deserialize_json(data["accountIds"])
    else:
        raise DeserializationError("BatchDeleteTaxRegistrationRequest.account_ids required")
    return out