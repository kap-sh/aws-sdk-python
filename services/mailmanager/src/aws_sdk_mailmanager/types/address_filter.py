"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddressFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address_prefix


class AddressFilter(TypedDict):
    address_prefix: NotRequired[
        "aws_sdk_mailmanager.types.address_prefix.AddressPrefix"
    ]
    """<p>Filter to limit the results to addresses having the provided prefix.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddressFilter) -> dict:
    out: dict = {}
    if "address_prefix" in value:
        out["AddressPrefix"] = value["address_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AddressFilter:
    out: AddressFilter = {}  # type: ignore[typeddict-item]
    if "AddressPrefix" in data:
        out["address_prefix"] = data["AddressPrefix"]
    return out
