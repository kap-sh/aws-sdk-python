"""Generated from Smithy shape ``com.amazonaws.appconfig#InvalidConfigurationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.string


class InvalidConfigurationDetail(TypedDict):
    constraint: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>The invalid or out-of-range validation constraint in your JSON schema that failed validation.</p>"""
    location: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>Location of the validation constraint in the configuration JSON schema that failed validation.</p>"""
    reason: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>The reason for an invalid configuration error.</p>"""
    type: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>The type of error for an invalid configuration.</p>"""
    value: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>Details about an error with Lambda when a synchronous extension experiences an error during an invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidConfigurationDetail) -> dict:
    out: dict = {}
    if "constraint" in value:
        out["Constraint"] = value["constraint"]
    if "location" in value:
        out["Location"] = value["location"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InvalidConfigurationDetail:
    out: InvalidConfigurationDetail = {}  # type: ignore[typeddict-item]
    if "Constraint" in data:
        out["constraint"] = data["Constraint"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
