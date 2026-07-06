"""Generated from Smithy shape ``com.amazonaws.opensearch#AdvancedSecurityOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.advanced_security_options
    import aws_sdk_opensearch.types.option_status


class AdvancedSecurityOptionsStatus(TypedDict, closed=True):
    options: (
        "aws_sdk_opensearch.types.advanced_security_options.AdvancedSecurityOptions"
    )
    """<p>Container for fine-grained access control settings.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>Status of the fine-grained access control settings for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.advanced_security_options

    out["Options"] = aws_sdk_opensearch.types.advanced_security_options.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptionsStatus:
    out: AdvancedSecurityOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.advanced_security_options

        out["options"] = (
            aws_sdk_opensearch.types.advanced_security_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("AdvancedSecurityOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AdvancedSecurityOptionsStatus.status required")
    return out
