"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddressFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.address_prefix


class AddressFilter(TypedDict, closed=True):
    address_prefix: NotRequired["capo_mailmanager.types.address_prefix.AddressPrefix"]
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
