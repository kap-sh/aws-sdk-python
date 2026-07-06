"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeAppVersionResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.physical_resource


class DescribeAppVersionResourceResponse(TypedDict, closed=True):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    physical_resource: NotRequired[
        "aws_sdk_resiliencehub.types.physical_resource.PhysicalResource"
    ]
    """<p>Defines a physical resource. A physical resource is a resource that exists in your account. It can be identified using an Amazon Resource Name (ARN) or a Resilience Hub-native identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppVersionResourceResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "physical_resource" in value:
        import aws_sdk_resiliencehub.types.physical_resource

        out["physicalResource"] = (
            aws_sdk_resiliencehub.types.physical_resource.serialize_json(
                value["physical_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppVersionResourceResponse:
    out: DescribeAppVersionResourceResponse = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourceResponse.app_arn required"
        )
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeAppVersionResourceResponse.app_version required"
        )
    if "physicalResource" in data:
        import aws_sdk_resiliencehub.types.physical_resource

        out["physical_resource"] = (
            aws_sdk_resiliencehub.types.physical_resource.deserialize_json(
                data["physicalResource"]
            )
        )
    return out
