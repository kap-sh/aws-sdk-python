"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DiffieHellmanDerivationData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.shared_information


class _DiffieHellmanDerivationData_SharedInformation(TypedDict):
    SharedInformation: (
        "aws_sdk_payment_cryptography_data.types.shared_information.SharedInformation"
    )


DiffieHellmanDerivationData: TypeAlias = _DiffieHellmanDerivationData_SharedInformation


# --- restJson1 ser/de ---
def serialize_json(value: DiffieHellmanDerivationData) -> dict:
    if "SharedInformation" in value:
        return {"SharedInformation": value["SharedInformation"]}
    else:
        raise SerializationError("DiffieHellmanDerivationData: no variant present")


def deserialize_json(data: dict) -> DiffieHellmanDerivationData:
    if "SharedInformation" in data:
        return {"SharedInformation": data["SharedInformation"]}
    else:
        raise DeserializationError(
            "DiffieHellmanDerivationData: no recognized variant key"
        )
