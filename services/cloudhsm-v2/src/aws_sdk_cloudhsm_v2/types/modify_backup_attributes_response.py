"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyBackupAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup


class ModifyBackupAttributesResponse(TypedDict, closed=True):
    backup: NotRequired["aws_sdk_cloudhsm_v2.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyBackupAttributesResponse) -> dict:
    out: dict = {}
    if "backup" in value:
        import aws_sdk_cloudhsm_v2.types.backup

        out["Backup"] = aws_sdk_cloudhsm_v2.types.backup.serialize_aws_json_1_1(
            value["backup"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyBackupAttributesResponse:
    out: ModifyBackupAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Backup" in data:
        import aws_sdk_cloudhsm_v2.types.backup

        out["backup"] = aws_sdk_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(
            data["Backup"]
        )
    return out
