"""Generated from Smithy shape ``com.amazonaws.opensearch#EncryptionAtRestOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.encryption_at_rest_options
    import aws_sdk_opensearch.types.option_status


class EncryptionAtRestOptionsStatus(TypedDict):
    options: (
        "aws_sdk_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
    )
    """<p>Encryption at rest options for the specified domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of the encryption at rest options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.encryption_at_rest_options

    out["Options"] = aws_sdk_opensearch.types.encryption_at_rest_options.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptionsStatus:
    out: EncryptionAtRestOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.encryption_at_rest_options

        out["options"] = (
            aws_sdk_opensearch.types.encryption_at_rest_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("EncryptionAtRestOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("EncryptionAtRestOptionsStatus.status required")
    return out
