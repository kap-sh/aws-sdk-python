"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteAccessControlConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_id
    import capo_kendra.types.index_id


class DeleteAccessControlConfigurationRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for an access control configuration.</p>"""
    id: "capo_kendra.types.access_control_configuration_id.AccessControlConfigurationId"
    """<p>The identifier of the access control configuration you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccessControlConfigurationRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccessControlConfigurationRequest:
    out: DeleteAccessControlConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "DeleteAccessControlConfigurationRequest.index_id required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "DeleteAccessControlConfigurationRequest.id required"
        )
    return out
