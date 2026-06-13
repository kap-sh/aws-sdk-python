"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_data_exports.types.execution_status_reason
    import aws_sdk_bcm_data_exports.types.export_status_code


class ExportStatus(TypedDict):
    status_code: NotRequired[
        "aws_sdk_bcm_data_exports.types.export_status_code.ExportStatusCode"
    ]
    """<p>The status code for the request.</p>"""
    status_reason: NotRequired[
        "aws_sdk_bcm_data_exports.types.execution_status_reason.ExecutionStatusReason"
    ]
    """<p>The description for the status code.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was updated.</p>"""
    last_refreshed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the export was last generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_bcm_data_exports.types.export_status_code

        out["StatusCode"] = (
            aws_sdk_bcm_data_exports.types.export_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_bcm_data_exports.types.execution_status_reason

        out["StatusReason"] = (
            aws_sdk_bcm_data_exports.types.execution_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "last_refreshed_at" in value:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["LastRefreshedAt"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["last_refreshed_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportStatus:
    out: ExportStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_bcm_data_exports.types.export_status_code

        out["status_code"] = (
            aws_sdk_bcm_data_exports.types.export_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_bcm_data_exports.types.execution_status_reason

        out["status_reason"] = (
            aws_sdk_bcm_data_exports.types.execution_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if "LastRefreshedAt" in data:
        import aws_sdk_bcm_data_exports.types._prelude.timestamp

        out["last_refreshed_at"] = (
            aws_sdk_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastRefreshedAt"]
            )
        )
    return out
