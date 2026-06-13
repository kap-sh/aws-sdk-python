"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchAssociateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.associate_configuration_request_list


class BatchAssociateCodeSecurityScanConfigurationRequest(TypedDict):
    associate_configuration_requests: "aws_sdk_inspector2.types.associate_configuration_request_list.AssociateConfigurationRequestList"
    """<p>A list of code repositories to associate with the specified scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.associate_configuration_request_list

    out["associateConfigurationRequests"] = (
        aws_sdk_inspector2.types.associate_configuration_request_list.serialize_json(
            value["associate_configuration_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAssociateCodeSecurityScanConfigurationRequest:
    out: BatchAssociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "associateConfigurationRequests" in data:
        import aws_sdk_inspector2.types.associate_configuration_request_list

        out["associate_configuration_requests"] = (
            aws_sdk_inspector2.types.associate_configuration_request_list.deserialize_json(
                data["associateConfigurationRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAssociateCodeSecurityScanConfigurationRequest.associate_configuration_requests required"
        )
    return out
