"""Generated from Smithy shape ``com.amazonaws.ssmsap#UpdateApplicationSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation_id_list


class UpdateApplicationSettingsOutput(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>The update message.</p>"""
    operation_ids: NotRequired[
        "aws_sdk_ssm_sap.types.operation_id_list.OperationIdList"
    ]
    """<p>The IDs of the operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationSettingsOutput) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "operation_ids" in value:
        import aws_sdk_ssm_sap.types.operation_id_list

        out["OperationIds"] = aws_sdk_ssm_sap.types.operation_id_list.serialize_json(
            value["operation_ids"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationSettingsOutput:
    out: UpdateApplicationSettingsOutput = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "OperationIds" in data:
        import aws_sdk_ssm_sap.types.operation_id_list

        out["operation_ids"] = aws_sdk_ssm_sap.types.operation_id_list.deserialize_json(
            data["OperationIds"]
        )
    return out
