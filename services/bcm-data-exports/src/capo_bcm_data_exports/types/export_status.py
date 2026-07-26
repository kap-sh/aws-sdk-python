"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExportStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_data_exports.types.execution_status_reason
    import capo_bcm_data_exports.types.export_status_code


class ExportStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_bcm_data_exports.types.export_status_code.ExportStatusCode"
    ]
    """<p>The status code for the request.</p>"""
    status_reason: NotRequired[
        "capo_bcm_data_exports.types.execution_status_reason.ExecutionStatusReason"
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
        import capo_bcm_data_exports.types.export_status_code

        out["StatusCode"] = (
            capo_bcm_data_exports.types.export_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        import capo_bcm_data_exports.types.execution_status_reason

        out["StatusReason"] = (
            capo_bcm_data_exports.types.execution_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "last_refreshed_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["LastRefreshedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["last_refreshed_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportStatus:
    out: ExportStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import capo_bcm_data_exports.types.export_status_code

        out["status_code"] = (
            capo_bcm_data_exports.types.export_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if "StatusReason" in data:
        import capo_bcm_data_exports.types.execution_status_reason

        out["status_reason"] = (
            capo_bcm_data_exports.types.execution_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if "CreatedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["created_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if "LastRefreshedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["last_refreshed_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastRefreshedAt"]
            )
        )
    return out
