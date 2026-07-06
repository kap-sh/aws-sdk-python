"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetHypervisorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.hypervisor_details


class GetHypervisorOutput(TypedDict, closed=True):
    hypervisor: NotRequired[
        "aws_sdk_backup_gateway.types.hypervisor_details.HypervisorDetails"
    ]
    """<p>Details about the requested hypervisor.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHypervisorOutput) -> dict:
    out: dict = {}
    if "hypervisor" in value:
        import aws_sdk_backup_gateway.types.hypervisor_details

        out["Hypervisor"] = (
            aws_sdk_backup_gateway.types.hypervisor_details.serialize_aws_json_1_0(
                value["hypervisor"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHypervisorOutput:
    out: GetHypervisorOutput = {}  # type: ignore[typeddict-item]
    if "Hypervisor" in data:
        import aws_sdk_backup_gateway.types.hypervisor_details

        out["hypervisor"] = (
            aws_sdk_backup_gateway.types.hypervisor_details.deserialize_aws_json_1_0(
                data["Hypervisor"]
            )
        )
    return out
