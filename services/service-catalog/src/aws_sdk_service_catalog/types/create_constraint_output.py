"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateConstraintOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.constraint_detail
    import aws_sdk_service_catalog.types.constraint_parameters
    import aws_sdk_service_catalog.types.status


class CreateConstraintOutput(TypedDict, closed=True):
    constraint_detail: NotRequired[
        "aws_sdk_service_catalog.types.constraint_detail.ConstraintDetail"
    ]
    """<p>Information about the constraint.</p>"""
    constraint_parameters: NotRequired[
        "aws_sdk_service_catalog.types.constraint_parameters.ConstraintParameters"
    ]
    """<p>The constraint parameters.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.status.Status"]
    """<p>The status of the current request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConstraintOutput) -> dict:
    out: dict = {}
    if "constraint_detail" in value:
        import aws_sdk_service_catalog.types.constraint_detail

        out["ConstraintDetail"] = (
            aws_sdk_service_catalog.types.constraint_detail.serialize_aws_json_1_1(
                value["constraint_detail"]
            )
        )
    if "constraint_parameters" in value:
        out["ConstraintParameters"] = value["constraint_parameters"]
    if "status" in value:
        import aws_sdk_service_catalog.types.status

        out["Status"] = aws_sdk_service_catalog.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConstraintOutput:
    out: CreateConstraintOutput = {}  # type: ignore[typeddict-item]
    if "ConstraintDetail" in data:
        import aws_sdk_service_catalog.types.constraint_detail

        out["constraint_detail"] = (
            aws_sdk_service_catalog.types.constraint_detail.deserialize_aws_json_1_1(
                data["ConstraintDetail"]
            )
        )
    if "ConstraintParameters" in data:
        out["constraint_parameters"] = data["ConstraintParameters"]
    if "Status" in data:
        import aws_sdk_service_catalog.types.status

        out["status"] = aws_sdk_service_catalog.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
