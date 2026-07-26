"""Generated from Smithy shape ``com.amazonaws.ssmsap#RegisterApplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.application
    import capo_ssm_sap.types.operation_id


class RegisterApplicationOutput(TypedDict, closed=True):
    application: NotRequired["capo_ssm_sap.types.application.Application"]
    """<p>The application registered with AWS Systems Manager for SAP.</p>"""
    operation_id: NotRequired["capo_ssm_sap.types.operation_id.OperationId"]
    """<p>The ID of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_ssm_sap.types.application

        out["Application"] = capo_ssm_sap.types.application.serialize_json(
            value["application"]
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> RegisterApplicationOutput:
    out: RegisterApplicationOutput = {}  # type: ignore[typeddict-item]
    if "Application" in data:
        import capo_ssm_sap.types.application

        out["application"] = capo_ssm_sap.types.application.deserialize_json(
            data["Application"]
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
