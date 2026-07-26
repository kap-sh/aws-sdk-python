"""Generated from Smithy shape ``com.amazonaws.kendra#AccessControlConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id


class AccessControlConfigurationSummary(TypedDict, closed=True):
    id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    """<p>The identifier of the access control configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlConfigurationSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessControlConfigurationSummary:
    out: AccessControlConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("AccessControlConfigurationSummary.id required")
    return out
