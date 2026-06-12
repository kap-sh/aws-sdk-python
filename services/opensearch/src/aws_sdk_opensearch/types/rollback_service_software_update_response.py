"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.rollback_service_software_options


class RollbackServiceSoftwareUpdateResponse(TypedDict):
    rollback_service_software_options: NotRequired[
        "aws_sdk_opensearch.types.rollback_service_software_options.RollbackServiceSoftwareOptions"
    ]
    """<p>The rollback options for the service software update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "rollback_service_software_options" in value:
        import aws_sdk_opensearch.types.rollback_service_software_options

        out["RollbackServiceSoftwareOptions"] = (
            aws_sdk_opensearch.types.rollback_service_software_options.serialize_json(
                value["rollback_service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> RollbackServiceSoftwareUpdateResponse:
    out: RollbackServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "RollbackServiceSoftwareOptions" in data:
        import aws_sdk_opensearch.types.rollback_service_software_options

        out["rollback_service_software_options"] = (
            aws_sdk_opensearch.types.rollback_service_software_options.deserialize_json(
                data["RollbackServiceSoftwareOptions"]
            )
        )
    return out
