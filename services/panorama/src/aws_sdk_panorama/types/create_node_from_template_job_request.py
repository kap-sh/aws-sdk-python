"""Generated from Smithy shape ``com.amazonaws.panorama#CreateNodeFromTemplateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.job_tags_list
    import aws_sdk_panorama.types.node_name
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.node_package_version
    import aws_sdk_panorama.types.template_parameters_map
    import aws_sdk_panorama.types.template_type


class CreateNodeFromTemplateJobRequest(TypedDict):
    template_type: "aws_sdk_panorama.types.template_type.TemplateType"
    """<p>The type of node.</p>"""
    output_package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>An output package name for the node.</p>"""
    output_package_version: (
        "aws_sdk_panorama.types.node_package_version.NodePackageVersion"
    )
    """<p>An output package version for the node.</p>"""
    node_name: "aws_sdk_panorama.types.node_name.NodeName"
    """<p>A name for the node.</p>"""
    node_description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>A description for the node.</p>"""
    template_parameters: (
        "aws_sdk_panorama.types.template_parameters_map.TemplateParametersMap"
    )
    """<p>Template parameters for the node.</p>"""
    job_tags: NotRequired["aws_sdk_panorama.types.job_tags_list.JobTagsList"]
    """<p>Tags for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeFromTemplateJobRequest) -> dict:
    out: dict = {}
    out["TemplateType"] = value["template_type"]
    out["OutputPackageName"] = value["output_package_name"]
    out["OutputPackageVersion"] = value["output_package_version"]
    out["NodeName"] = value["node_name"]
    if "node_description" in value:
        out["NodeDescription"] = value["node_description"]
    import aws_sdk_panorama.types.template_parameters_map

    out["TemplateParameters"] = (
        aws_sdk_panorama.types.template_parameters_map.serialize_json(
            value["template_parameters"]
        )
    )
    if "job_tags" in value:
        import aws_sdk_panorama.types.job_tags_list

        out["JobTags"] = aws_sdk_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodeFromTemplateJobRequest:
    out: CreateNodeFromTemplateJobRequest = {}  # type: ignore[typeddict-item]
    if "TemplateType" in data:
        out["template_type"] = data["TemplateType"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.template_type required"
        )
    if "OutputPackageName" in data:
        out["output_package_name"] = data["OutputPackageName"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.output_package_name required"
        )
    if "OutputPackageVersion" in data:
        out["output_package_version"] = data["OutputPackageVersion"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.output_package_version required"
        )
    if "NodeName" in data:
        out["node_name"] = data["NodeName"]
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.node_name required"
        )
    if "NodeDescription" in data:
        out["node_description"] = data["NodeDescription"]
    if "TemplateParameters" in data:
        import aws_sdk_panorama.types.template_parameters_map

        out["template_parameters"] = (
            aws_sdk_panorama.types.template_parameters_map.deserialize_json(
                data["TemplateParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNodeFromTemplateJobRequest.template_parameters required"
        )
    if "JobTags" in data:
        import aws_sdk_panorama.types.job_tags_list

        out["job_tags"] = aws_sdk_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out
