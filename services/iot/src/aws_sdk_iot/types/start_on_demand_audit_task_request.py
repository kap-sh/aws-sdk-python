"""Generated from Smithy shape ``com.amazonaws.iot#StartOnDemandAuditTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.target_audit_check_names


class StartOnDemandAuditTaskRequest(TypedDict):
    target_check_names: (
        "aws_sdk_iot.types.target_audit_check_names.TargetAuditCheckNames"
    )
    """<p>Which checks are performed during the audit. The checks you specify must be enabled for your account or an exception occurs. Use <code>DescribeAccountAuditConfiguration</code> to see the list of all checks, including those that are enabled or <code>UpdateAccountAuditConfiguration</code> to select which checks are enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOnDemandAuditTaskRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.target_audit_check_names

    out["targetCheckNames"] = aws_sdk_iot.types.target_audit_check_names.serialize_json(
        value["target_check_names"]
    )
    return out


def deserialize_json(data: dict) -> StartOnDemandAuditTaskRequest:
    out: StartOnDemandAuditTaskRequest = {}  # type: ignore[typeddict-item]
    if "targetCheckNames" in data:
        import aws_sdk_iot.types.target_audit_check_names

        out["target_check_names"] = (
            aws_sdk_iot.types.target_audit_check_names.deserialize_json(
                data["targetCheckNames"]
            )
        )
    else:
        raise DeserializationError(
            "StartOnDemandAuditTaskRequest.target_check_names required"
        )
    return out
