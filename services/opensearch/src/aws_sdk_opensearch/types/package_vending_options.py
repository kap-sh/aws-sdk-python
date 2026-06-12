"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageVendingOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean


class PackageVendingOptions(TypedDict):
    vending_enabled: "aws_sdk_opensearch.types.boolean.Boolean"
    """<p>Indicates whether the package vending feature is enabled, allowing the package to be used by other users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVendingOptions) -> dict:
    out: dict = {}
    out["VendingEnabled"] = value["vending_enabled"]
    return out


def deserialize_json(data: dict) -> PackageVendingOptions:
    out: PackageVendingOptions = {}  # type: ignore[typeddict-item]
    if "VendingEnabled" in data:
        out["vending_enabled"] = data["VendingEnabled"]
    else:
        raise DeserializationError("PackageVendingOptions.vending_enabled required")
    return out
