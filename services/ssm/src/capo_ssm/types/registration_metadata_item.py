"""Generated from Smithy shape ``com.amazonaws.ssm#RegistrationMetadataItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.registration_metadata_key
    import capo_ssm.types.registration_metadata_value


class RegistrationMetadataItem(TypedDict, closed=True):
    key: "capo_ssm.types.registration_metadata_key.RegistrationMetadataKey"
    """<p>Reserved for internal use.</p>"""
    value: "capo_ssm.types.registration_metadata_value.RegistrationMetadataValue"
    """<p>Reserved for internal use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistrationMetadataItem) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistrationMetadataItem:
    out: RegistrationMetadataItem = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("RegistrationMetadataItem.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("RegistrationMetadataItem.value required")
    return out
