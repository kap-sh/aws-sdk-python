"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchRevokePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.batch_permissions_failure_list


class BatchRevokePermissionsResponse(TypedDict):
    failures: NotRequired[
        "aws_sdk_lakeformation.types.batch_permissions_failure_list.BatchPermissionsFailureList"
    ]
    """<p>A list of failures to revoke permissions to the resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokePermissionsResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_lakeformation.types.batch_permissions_failure_list

        out["Failures"] = (
            aws_sdk_lakeformation.types.batch_permissions_failure_list.serialize_json(
                value["failures"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchRevokePermissionsResponse:
    out: BatchRevokePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import aws_sdk_lakeformation.types.batch_permissions_failure_list

        out["failures"] = (
            aws_sdk_lakeformation.types.batch_permissions_failure_list.deserialize_json(
                data["Failures"]
            )
        )
    return out
