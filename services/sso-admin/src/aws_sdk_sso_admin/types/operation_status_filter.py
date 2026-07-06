"""Generated from Smithy shape ``com.amazonaws.ssoadmin#OperationStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.status_values


class OperationStatusFilter(TypedDict, closed=True):
    status: NotRequired["aws_sdk_sso_admin.types.status_values.StatusValues"]
    """<p>Filters the list operations result based on the status attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatusFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sso_admin.types.status_values

        out["Status"] = aws_sdk_sso_admin.types.status_values.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationStatusFilter:
    out: OperationStatusFilter = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sso_admin.types.status_values

        out["status"] = aws_sdk_sso_admin.types.status_values.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
