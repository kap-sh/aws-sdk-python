"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ImportResourcesToDraftAppVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.arn_list
    import aws_sdk_resiliencehub.types.eks_source_list
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.resource_import_status_type
    import aws_sdk_resiliencehub.types.terraform_source_list


class ImportResourcesToDraftAppVersionResponse(TypedDict, closed=True):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    source_arns: NotRequired["aws_sdk_resiliencehub.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARNs) for the resources you have imported.</p>"""
    status: "aws_sdk_resiliencehub.types.resource_import_status_type.ResourceImportStatusType"
    """<p>Status of the action.</p>"""
    terraform_sources: NotRequired[
        "aws_sdk_resiliencehub.types.terraform_source_list.TerraformSourceList"
    ]
    """<p> A list of terraform file s3 URLs you have imported. </p>"""
    eks_sources: NotRequired[
        "aws_sdk_resiliencehub.types.eks_source_list.EksSourceList"
    ]
    """<p>The input sources of the Amazon Elastic Kubernetes Service resources you have imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportResourcesToDraftAppVersionResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "source_arns" in value:
        import aws_sdk_resiliencehub.types.arn_list

        out["sourceArns"] = aws_sdk_resiliencehub.types.arn_list.serialize_json(
            value["source_arns"]
        )
    import aws_sdk_resiliencehub.types.resource_import_status_type

    out["status"] = (
        aws_sdk_resiliencehub.types.resource_import_status_type.serialize_json(
            value["status"]
        )
    )
    if "terraform_sources" in value:
        import aws_sdk_resiliencehub.types.terraform_source_list

        out["terraformSources"] = (
            aws_sdk_resiliencehub.types.terraform_source_list.serialize_json(
                value["terraform_sources"]
            )
        )
    if "eks_sources" in value:
        import aws_sdk_resiliencehub.types.eks_source_list

        out["eksSources"] = aws_sdk_resiliencehub.types.eks_source_list.serialize_json(
            value["eks_sources"]
        )
    return out


def deserialize_json(data: dict) -> ImportResourcesToDraftAppVersionResponse:
    out: ImportResourcesToDraftAppVersionResponse = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "ImportResourcesToDraftAppVersionResponse.app_arn required"
        )
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "ImportResourcesToDraftAppVersionResponse.app_version required"
        )
    if "sourceArns" in data:
        import aws_sdk_resiliencehub.types.arn_list

        out["source_arns"] = aws_sdk_resiliencehub.types.arn_list.deserialize_json(
            data["sourceArns"]
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.resource_import_status_type

        out["status"] = (
            aws_sdk_resiliencehub.types.resource_import_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "ImportResourcesToDraftAppVersionResponse.status required"
        )
    if "terraformSources" in data:
        import aws_sdk_resiliencehub.types.terraform_source_list

        out["terraform_sources"] = (
            aws_sdk_resiliencehub.types.terraform_source_list.deserialize_json(
                data["terraformSources"]
            )
        )
    if "eksSources" in data:
        import aws_sdk_resiliencehub.types.eks_source_list

        out["eks_sources"] = (
            aws_sdk_resiliencehub.types.eks_source_list.deserialize_json(
                data["eksSources"]
            )
        )
    return out
