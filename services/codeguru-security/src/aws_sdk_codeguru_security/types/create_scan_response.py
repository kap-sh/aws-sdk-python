"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CreateScanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.resource_id
    import aws_sdk_codeguru_security.types.scan_name
    import aws_sdk_codeguru_security.types.scan_name_arn
    import aws_sdk_codeguru_security.types.scan_state
    import aws_sdk_codeguru_security.types.uuid


class CreateScanResponse(TypedDict):
    scan_name: "aws_sdk_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan.</p>"""
    run_id: "aws_sdk_codeguru_security.types.uuid.Uuid"
    """<p>UUID that identifies the individual scan run.</p>"""
    resource_id: "aws_sdk_codeguru_security.types.resource_id.ResourceId"
    """<p>The identifier for the resource object that contains resources that were scanned.</p>"""
    scan_state: "aws_sdk_codeguru_security.types.scan_state.ScanState"
    """<p>The current state of the scan. Returns either <code>InProgress</code>, <code>Successful</code>, or <code>Failed</code>.</p>"""
    scan_name_arn: NotRequired[
        "aws_sdk_codeguru_security.types.scan_name_arn.ScanNameArn"
    ]
    """<p>The ARN for the scan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScanResponse) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["runId"] = value["run_id"]
    import aws_sdk_codeguru_security.types.resource_id

    out["resourceId"] = aws_sdk_codeguru_security.types.resource_id.serialize_json(
        value["resource_id"]
    )
    import aws_sdk_codeguru_security.types.scan_state

    out["scanState"] = aws_sdk_codeguru_security.types.scan_state.serialize_json(
        value["scan_state"]
    )
    if "scan_name_arn" in value:
        out["scanNameArn"] = value["scan_name_arn"]
    return out


def deserialize_json(data: dict) -> CreateScanResponse:
    out: CreateScanResponse = {}  # type: ignore[typeddict-item]
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    else:
        raise DeserializationError("CreateScanResponse.scan_name required")
    if "runId" in data:
        out["run_id"] = data["runId"]
    else:
        raise DeserializationError("CreateScanResponse.run_id required")
    if "resourceId" in data:
        import aws_sdk_codeguru_security.types.resource_id

        out["resource_id"] = (
            aws_sdk_codeguru_security.types.resource_id.deserialize_json(
                data["resourceId"]
            )
        )
    else:
        raise DeserializationError("CreateScanResponse.resource_id required")
    if "scanState" in data:
        import aws_sdk_codeguru_security.types.scan_state

        out["scan_state"] = aws_sdk_codeguru_security.types.scan_state.deserialize_json(
            data["scanState"]
        )
    else:
        raise DeserializationError("CreateScanResponse.scan_state required")
    if "scanNameArn" in data:
        out["scan_name_arn"] = data["scanNameArn"]
    return out
