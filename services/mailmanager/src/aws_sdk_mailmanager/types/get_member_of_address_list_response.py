"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetMemberOfAddressListResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.address


class GetMemberOfAddressListResponse(TypedDict):
    address: "aws_sdk_mailmanager.types.address.Address"
    """<p>The address retrieved from the address list.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMemberOfAddressListResponse) -> dict:
    out: dict = {}
    out["Address"] = value["address"]
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMemberOfAddressListResponse:
    out: GetMemberOfAddressListResponse = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("GetMemberOfAddressListResponse.address required")
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "GetMemberOfAddressListResponse.created_timestamp required"
        )
    return out
