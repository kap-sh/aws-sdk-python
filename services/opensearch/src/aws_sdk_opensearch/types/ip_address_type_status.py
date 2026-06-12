"""Generated from Smithy shape ``com.amazonaws.opensearch#IPAddressTypeStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.ip_address_type
    import aws_sdk_opensearch.types.option_status


class IPAddressTypeStatus(TypedDict):
    options: "aws_sdk_opensearch.types.ip_address_type.IPAddressType"
    """<p>The IP address options for the domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"


# --- restJson1 ser/de ---
def serialize_json(value: IPAddressTypeStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.ip_address_type

    out["Options"] = aws_sdk_opensearch.types.ip_address_type.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> IPAddressTypeStatus:
    out: IPAddressTypeStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.ip_address_type

        out["options"] = aws_sdk_opensearch.types.ip_address_type.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("IPAddressTypeStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("IPAddressTypeStatus.status required")
    return out
