"""Generated from Smithy shape ``com.amazonaws.opensearch#IdentityCenterOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.identity_center_options
    import aws_sdk_opensearch.types.option_status


class IdentityCenterOptionsStatus(TypedDict):
    options: "aws_sdk_opensearch.types.identity_center_options.IdentityCenterOptions"
    """<p>Configuration settings for IAM Identity Center integration.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of IAM Identity Center configuration settings for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.identity_center_options

    out["Options"] = aws_sdk_opensearch.types.identity_center_options.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> IdentityCenterOptionsStatus:
    out: IdentityCenterOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.identity_center_options

        out["options"] = (
            aws_sdk_opensearch.types.identity_center_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("IdentityCenterOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("IdentityCenterOptionsStatus.status required")
    return out
