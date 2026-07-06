"""Generated from Smithy shape ``com.amazonaws.glue#StatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.table
    import aws_sdk_glue.types.view_validation_list


class StatusDetails(TypedDict, closed=True):
    requested_change: NotRequired["aws_sdk_glue.types.table.Table"]
    """<p>A <code>Table</code> object representing the requested changes.</p>"""
    view_validations: NotRequired[
        "aws_sdk_glue.types.view_validation_list.ViewValidationList"
    ]
    """<p>A list of <code>ViewValidation</code> objects that contain information for an analytical engine to validate a view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusDetails) -> dict:
    out: dict = {}
    if "requested_change" in value:
        import aws_sdk_glue.types.table

        out["RequestedChange"] = aws_sdk_glue.types.table.serialize_aws_json_1_1(
            value["requested_change"]
        )
    if "view_validations" in value:
        import aws_sdk_glue.types.view_validation_list

        out["ViewValidations"] = (
            aws_sdk_glue.types.view_validation_list.serialize_aws_json_1_1(
                value["view_validations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatusDetails:
    out: StatusDetails = {}  # type: ignore[typeddict-item]
    if "RequestedChange" in data:
        import aws_sdk_glue.types.table

        out["requested_change"] = aws_sdk_glue.types.table.deserialize_aws_json_1_1(
            data["RequestedChange"]
        )
    if "ViewValidations" in data:
        import aws_sdk_glue.types.view_validation_list

        out["view_validations"] = (
            aws_sdk_glue.types.view_validation_list.deserialize_aws_json_1_1(
                data["ViewValidations"]
            )
        )
    return out
