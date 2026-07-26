"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.operation


class GetOperationOutput(TypedDict, closed=True):
    operation: NotRequired["capo_ssm_sap.types.operation.Operation"]
    """<p>Returns the details of an operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOperationOutput) -> dict:
    out: dict = {}
    if "operation" in value:
        import capo_ssm_sap.types.operation

        out["Operation"] = capo_ssm_sap.types.operation.serialize_json(
            value["operation"]
        )
    return out


def deserialize_json(data: dict) -> GetOperationOutput:
    out: GetOperationOutput = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        import capo_ssm_sap.types.operation

        out["operation"] = capo_ssm_sap.types.operation.deserialize_json(
            data["Operation"]
        )
    return out
