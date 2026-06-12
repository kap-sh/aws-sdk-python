"""Generated from Smithy shape ``com.amazonaws.opensearch#DryRunProgressStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.validation_failures


class DryRunProgressStatus(TypedDict):
    dry_run_id: "aws_sdk_opensearch.types.guid.GUID"
    """<p>The unique identifier of the dry run.</p>"""
    dry_run_status: "aws_sdk_opensearch.types.string.String"
    """<p>The current status of the dry run.</p>"""
    creation_date: "aws_sdk_opensearch.types.string.String"
    """<p>The timestamp when the dry run was initiated.</p>"""
    update_date: "aws_sdk_opensearch.types.string.String"
    """<p>The timestamp when the dry run was last updated.</p>"""
    validation_failures: NotRequired[
        "aws_sdk_opensearch.types.validation_failures.ValidationFailures"
    ]
    """<p>Any validation failures that occurred as a result of the dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DryRunProgressStatus) -> dict:
    out: dict = {}
    out["DryRunId"] = value["dry_run_id"]
    out["DryRunStatus"] = value["dry_run_status"]
    out["CreationDate"] = value["creation_date"]
    out["UpdateDate"] = value["update_date"]
    if "validation_failures" in value:
        import aws_sdk_opensearch.types.validation_failures

        out["ValidationFailures"] = (
            aws_sdk_opensearch.types.validation_failures.serialize_json(
                value["validation_failures"]
            )
        )
    return out


def deserialize_json(data: dict) -> DryRunProgressStatus:
    out: DryRunProgressStatus = {}  # type: ignore[typeddict-item]
    if "DryRunId" in data:
        out["dry_run_id"] = data["DryRunId"]
    else:
        raise DeserializationError("DryRunProgressStatus.dry_run_id required")
    if "DryRunStatus" in data:
        out["dry_run_status"] = data["DryRunStatus"]
    else:
        raise DeserializationError("DryRunProgressStatus.dry_run_status required")
    if "CreationDate" in data:
        out["creation_date"] = data["CreationDate"]
    else:
        raise DeserializationError("DryRunProgressStatus.creation_date required")
    if "UpdateDate" in data:
        out["update_date"] = data["UpdateDate"]
    else:
        raise DeserializationError("DryRunProgressStatus.update_date required")
    if "ValidationFailures" in data:
        import aws_sdk_opensearch.types.validation_failures

        out["validation_failures"] = (
            aws_sdk_opensearch.types.validation_failures.deserialize_json(
                data["ValidationFailures"]
            )
        )
    return out
