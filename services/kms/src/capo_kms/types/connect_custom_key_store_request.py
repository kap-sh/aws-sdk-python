"""Generated from Smithy shape ``com.amazonaws.kms#ConnectCustomKeyStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.custom_key_store_id_type


class ConnectCustomKeyStoreRequest(TypedDict, closed=True):
    custom_key_store_id: "capo_kms.types.custom_key_store_id_type.CustomKeyStoreIdType"
    """<p>Enter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the <a>DescribeCustomKeyStores</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectCustomKeyStoreRequest) -> dict:
    out: dict = {}
    out["CustomKeyStoreId"] = value["custom_key_store_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectCustomKeyStoreRequest:
    out: ConnectCustomKeyStoreRequest = {}  # type: ignore[typeddict-item]
    if "CustomKeyStoreId" in data:
        out["custom_key_store_id"] = data["CustomKeyStoreId"]
    else:
        raise DeserializationError(
            "ConnectCustomKeyStoreRequest.custom_key_store_id required"
        )
    return out
