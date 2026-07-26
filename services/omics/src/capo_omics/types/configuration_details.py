"""Generated from Smithy shape ``com.amazonaws.omics#ConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.configuration_arn
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_uuid


class ConfigurationDetails(TypedDict, closed=True):
    name: NotRequired["capo_omics.types.configuration_name.ConfigurationName"]
    """<p>User-friendly name for the configuration.</p>"""
    arn: NotRequired["capo_omics.types.configuration_arn.ConfigurationArn"]
    """<p>Unique resource identifier for the configuration.</p>"""
    uuid: NotRequired["capo_omics.types.configuration_uuid.ConfigurationUuid"]
    """<p>Unique identifier for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    return out


def deserialize_json(data: dict) -> ConfigurationDetails:
    out: ConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    return out
