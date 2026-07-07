"""Generated from Smithy shape ``com.amazonaws.fms#GetViolationDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.violation_detail


class GetViolationDetailsResponse(TypedDict, closed=True):
    violation_detail: NotRequired["aws_sdk_fms.types.violation_detail.ViolationDetail"]
    """<p>Violation detail for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetViolationDetailsResponse) -> dict:
    out: dict = {}
    if "violation_detail" in value:
        import aws_sdk_fms.types.violation_detail

        out["ViolationDetail"] = (
            aws_sdk_fms.types.violation_detail.serialize_aws_json_1_1(
                value["violation_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetViolationDetailsResponse:
    out: GetViolationDetailsResponse = {}  # type: ignore[typeddict-item]
    if "ViolationDetail" in data:
        import aws_sdk_fms.types.violation_detail

        out["violation_detail"] = (
            aws_sdk_fms.types.violation_detail.deserialize_aws_json_1_1(
                data["ViolationDetail"]
            )
        )
    return out
