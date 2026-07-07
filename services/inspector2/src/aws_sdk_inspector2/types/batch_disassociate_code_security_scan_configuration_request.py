"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchDisassociateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.disassociate_configuration_request_list


class BatchDisassociateCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    disassociate_configuration_requests: "aws_sdk_inspector2.types.disassociate_configuration_request_list.DisassociateConfigurationRequestList"
    """<p>A list of code repositories to disassociate from the specified scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: BatchDisassociateCodeSecurityScanConfigurationRequest,
) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.disassociate_configuration_request_list

    out["disassociateConfigurationRequests"] = (
        aws_sdk_inspector2.types.disassociate_configuration_request_list.serialize_json(
            value["disassociate_configuration_requests"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> BatchDisassociateCodeSecurityScanConfigurationRequest:
    out: BatchDisassociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "disassociateConfigurationRequests" in data:
        import aws_sdk_inspector2.types.disassociate_configuration_request_list

        out["disassociate_configuration_requests"] = (
            aws_sdk_inspector2.types.disassociate_configuration_request_list.deserialize_json(
                data["disassociateConfigurationRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDisassociateCodeSecurityScanConfigurationRequest.disassociate_configuration_requests required"
        )
    return out
