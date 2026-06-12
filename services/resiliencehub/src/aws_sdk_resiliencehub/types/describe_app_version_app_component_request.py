"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppVersionAppComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.string255


class DescribeAppVersionAppComponentRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    id: "aws_sdk_resiliencehub.types.string255.String255"
    """<p>Identifier of the Application Component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppVersionAppComponentRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DescribeAppVersionAppComponentRequest:
    out: DescribeAppVersionAppComponentRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeAppVersionAppComponentRequest.app_arn required"
        )
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeAppVersionAppComponentRequest.app_version required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DescribeAppVersionAppComponentRequest.id required")
    return out
