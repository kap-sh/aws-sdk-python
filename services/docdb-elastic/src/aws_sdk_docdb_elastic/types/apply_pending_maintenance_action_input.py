"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ApplyPendingMaintenanceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.input_string
    import aws_sdk_docdb_elastic.types.opt_in_type


class ApplyPendingMaintenanceActionInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_docdb_elastic.types.input_string.InputString"
    """<p>The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.</p>"""
    apply_action: "aws_sdk_docdb_elastic.types.input_string.InputString"
    """<p>The pending maintenance action to apply to the resource.</p> <p>Valid actions are:</p> <ul> <li> <p> <code>ENGINE_UPDATE<i/> </code> </p> </li> <li> <p> <code>ENGINE_UPGRADE</code> </p> </li> <li> <p> <code>SECURITY_UPDATE</code> </p> </li> <li> <p> <code>OS_UPDATE</code> </p> </li> <li> <p> <code>MASTER_USER_PASSWORD_UPDATE</code> </p> </li> </ul>"""
    opt_in_type: "aws_sdk_docdb_elastic.types.opt_in_type.OptInType"
    """<p>A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type <code>IMMEDIATE</code> can't be undone.</p>"""
    apply_on: NotRequired["aws_sdk_docdb_elastic.types.input_string.InputString"]
    """<p>A specific date to apply the pending maintenance action. Required if opt-in-type is <code>APPLY_ON</code>. Format: <code>yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyPendingMaintenanceActionInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["applyAction"] = value["apply_action"]
    out["optInType"] = value["opt_in_type"]
    if "apply_on" in value:
        out["applyOn"] = value["apply_on"]
    return out


def deserialize_json(data: dict) -> ApplyPendingMaintenanceActionInput:
    out: ApplyPendingMaintenanceActionInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionInput.resource_arn required"
        )
    if "applyAction" in data:
        out["apply_action"] = data["applyAction"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionInput.apply_action required"
        )
    if "optInType" in data:
        out["opt_in_type"] = data["optInType"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionInput.opt_in_type required"
        )
    if "applyOn" in data:
        out["apply_on"] = data["applyOn"]
    return out
