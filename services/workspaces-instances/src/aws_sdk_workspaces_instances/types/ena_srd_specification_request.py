"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EnaSrdSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request


class EnaSrdSpecificationRequest(TypedDict):
    ena_srd_enabled: NotRequired["bool"]
    """<p>Enables or disables ENA SRD for network performance.</p>"""
    ena_srd_udp_specification: NotRequired[
        "aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request.EnaSrdUdpSpecificationRequest"
    ]
    """<p>Configures UDP-specific ENA SRD settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnaSrdSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_enabled" in value:
        out["EnaSrdEnabled"] = value["ena_srd_enabled"]
    if "ena_srd_udp_specification" in value:
        import aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request

        out["EnaSrdUdpSpecification"] = (
            aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request.serialize_aws_json_1_0(
                value["ena_srd_udp_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnaSrdSpecificationRequest:
    out: EnaSrdSpecificationRequest = {}  # type: ignore[typeddict-item]
    if "EnaSrdEnabled" in data:
        out["ena_srd_enabled"] = data["EnaSrdEnabled"]
    if "EnaSrdUdpSpecification" in data:
        import aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request

        out["ena_srd_udp_specification"] = (
            aws_sdk_workspaces_instances.types.ena_srd_udp_specification_request.deserialize_aws_json_1_0(
                data["EnaSrdUdpSpecification"]
            )
        )
    return out
