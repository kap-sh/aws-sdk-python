"""Generated from Smithy shape ``com.amazonaws.snowball#CreateAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address


class CreateAddressRequest(TypedDict):
    address: "aws_sdk_snowball.types.address.Address"
    """<p>The address that you want the Snow device shipped to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAddressRequest) -> dict:
    out: dict = {}
    import aws_sdk_snowball.types.address

    out["Address"] = aws_sdk_snowball.types.address.serialize_aws_json_1_1(
        value["address"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAddressRequest:
    out: CreateAddressRequest = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        import aws_sdk_snowball.types.address

        out["address"] = aws_sdk_snowball.types.address.deserialize_aws_json_1_1(
            data["Address"]
        )
    else:
        raise DeserializationError("CreateAddressRequest.address required")
    return out
