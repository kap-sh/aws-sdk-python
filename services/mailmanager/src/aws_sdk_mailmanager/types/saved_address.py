"""Generated from Smithy shape ``com.amazonaws.mailmanager#SavedAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.address


class SavedAddress(TypedDict, closed=True):
    address: "aws_sdk_mailmanager.types.address.Address"
    """<p>The email or domain that constitutes the address.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the address was added to the address list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavedAddress) -> dict:
    out: dict = {}
    out["Address"] = value["address"]
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavedAddress:
    out: SavedAddress = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    else:
        raise DeserializationError("SavedAddress.address required")
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("SavedAddress.created_timestamp required")
    return out
