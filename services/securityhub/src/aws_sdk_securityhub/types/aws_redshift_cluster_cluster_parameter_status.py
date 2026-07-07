"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterParameterStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterParameterStatus(TypedDict, closed=True):
    parameter_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the parameter.</p>"""
    parameter_apply_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the parameter. Indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when it was applied.</p> <p>Valid values: <code>in-sync</code> | <code>pending-reboot</code> | <code>applying</code> | <code>invalid-parameter</code> | <code>apply-deferred</code> | <code>apply-error</code> | <code>unknown-error</code> </p>"""
    parameter_apply_error_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The error that prevented the parameter from being applied to the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterParameterStatus) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_apply_status" in value:
        out["ParameterApplyStatus"] = value["parameter_apply_status"]
    if "parameter_apply_error_description" in value:
        out["ParameterApplyErrorDescription"] = value[
            "parameter_apply_error_description"
        ]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterParameterStatus:
    out: AwsRedshiftClusterClusterParameterStatus = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "ParameterApplyStatus" in data:
        out["parameter_apply_status"] = data["ParameterApplyStatus"]
    if "ParameterApplyErrorDescription" in data:
        out["parameter_apply_error_description"] = data[
            "ParameterApplyErrorDescription"
        ]
    return out
