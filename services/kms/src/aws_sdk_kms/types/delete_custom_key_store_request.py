"""Generated from Smithy shape ``com.amazonaws.kms#DeleteCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_kms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kms.types.custom_key_store_id_type


class DeleteCustomKeyStoreRequest(TypedDict):
    custom_key_store_id: (
        "aws_sdk_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    )
    """<p>Enter the ID of the custom key store you want to delete. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCustomKeyStoreRequest) -> dict:
    out: dict = {}
    out["CustomKeyStoreId"] = value["custom_key_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCustomKeyStoreRequest:
    out: DeleteCustomKeyStoreRequest = {}  # type: ignore[typeddict-item]
    if "CustomKeyStoreId" in data:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    else:
        raise DeserializationError(
            "DeleteCustomKeyStoreRequest.custom_key_store_id required"
        )
    return out
