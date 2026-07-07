"""Generated from Smithy shape ``com.amazonaws.kms#CreateCustomKeyStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_store_id_type


class CreateCustomKeyStoreResponse(TypedDict, closed=True):
    custom_key_store_id: NotRequired[
        "aws_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    ]
    """<p>A unique identifier for the new custom key store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomKeyStoreResponse) -> dict:
    out: dict = {}
    if "custom_key_store_id" in value:
        out["CustomKeyStoreId"] = value["custom_key_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomKeyStoreResponse:
    out: CreateCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    if "CustomKeyStoreId" in data:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    return out
