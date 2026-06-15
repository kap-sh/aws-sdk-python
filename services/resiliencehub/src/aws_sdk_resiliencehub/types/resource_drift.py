"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceDrift``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.difference_type
    import aws_sdk_resiliencehub.types.entity_id
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.resource_identifier


class ResourceDrift(TypedDict):
    app_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    r"""<p>Amazon Resource Name (ARN) of the application whose resources have drifted. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: NotRequired["aws_sdk_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Version of the application whose resources have drifted.</p>"""
    reference_id: NotRequired["aws_sdk_resiliencehub.types.entity_id.EntityId"]
    """<p>Reference identifier of the resource drift.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_resiliencehub.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Identifier of the drifted resource.</p>"""
    diff_type: NotRequired["aws_sdk_resiliencehub.types.difference_type.DifferenceType"]
    """<p>Indicates if the resource was added or removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDrift) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_version" in value:
        out["appVersion"] = value["app_version"]
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    if "resource_identifier" in value:
        import aws_sdk_resiliencehub.types.resource_identifier

        out["resourceIdentifier"] = (
            aws_sdk_resiliencehub.types.resource_identifier.serialize_json(
                value["resource_identifier"]
            )
        )
    if "diff_type" in value:
        import aws_sdk_resiliencehub.types.difference_type

        out["diffType"] = aws_sdk_resiliencehub.types.difference_type.serialize_json(
            value["diff_type"]
        )
    return out


def deserialize_json(data: dict) -> ResourceDrift:
    out: ResourceDrift = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    if "referenceId" in data:
        out["reference_id"] = data["referenceId"]
    if "resourceIdentifier" in data:
        import aws_sdk_resiliencehub.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_resiliencehub.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if "diffType" in data:
        import aws_sdk_resiliencehub.types.difference_type

        out["diff_type"] = aws_sdk_resiliencehub.types.difference_type.deserialize_json(
            data["diffType"]
        )
    return out
