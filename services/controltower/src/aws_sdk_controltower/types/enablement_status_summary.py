"""Generated from Smithy shape ``com.amazonaws.controltower#EnablementStatusSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enablement_status
    import aws_sdk_controltower.types.operation_identifier


class EnablementStatusSummary(TypedDict):
    status: NotRequired["aws_sdk_controltower.types.enablement_status.EnablementStatus"]
    """<p> The deployment status of the enabled resource.</p> <p>Valid values:</p> <ul> <li> <p> <code>SUCCEEDED</code>: The <code>EnabledControl</code> or <code>EnabledBaseline</code> configuration was deployed successfully.</p> </li> <li> <p> <code>UNDER_CHANGE</code>: The <code>EnabledControl</code> or <code>EnabledBaseline</code> configuration is changing. </p> </li> <li> <p> <code>FAILED</code>: The <code>EnabledControl</code> or <code>EnabledBaseline</code> configuration failed to deploy.</p> </li> </ul>"""
    last_operation_identifier: NotRequired[
        "aws_sdk_controltower.types.operation_identifier.OperationIdentifier"
    ]
    """<p>The last operation identifier for the enabled resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnablementStatusSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_controltower.types.enablement_status

        out["status"] = aws_sdk_controltower.types.enablement_status.serialize_json(
            value["status"]
        )
    if "last_operation_identifier" in value:
        out["lastOperationIdentifier"] = value["last_operation_identifier"]
    return out


def deserialize_json(data: dict) -> EnablementStatusSummary:
    out: EnablementStatusSummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_controltower.types.enablement_status

        out["status"] = aws_sdk_controltower.types.enablement_status.deserialize_json(
            data["status"]
        )
    if "lastOperationIdentifier" in data:
        out["last_operation_identifier"] = data["lastOperationIdentifier"]
    return out
